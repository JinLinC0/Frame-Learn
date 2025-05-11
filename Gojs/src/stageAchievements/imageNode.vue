<template>
    <div class="common-layout">
        <div class="layout-container">
            <div id="PaletteDiv" class="layout-aside">
                 <div id="svg_zhaChi" class="svg_class" draggable="true" @dragstart="dragstart">
                    <img id="svg_zhaChi" src="./pid_node/渣池.svg">
                 </div>
                 <div id="html" style="background-color: aqua; width: 100px; height: 100px; margin-left: auto; margin-right: auto;" draggable="true" @dragstart="dragstart">html元素</div>
                 <div class="pipeClass">
                    <span style="margin: 5px;">管道</span>
                    <div id="pipe" style="background-color: gray; width: 30px; height: 30px; margin: 5px;" draggable="true" @dragstart="dragstart"></div>
                 </div>
            </div>
            <div id="diagramDiv" class="layout-main" @dragover="event => event.preventDefault()"
                @dragenter="event => event.preventDefault()" @drop="drop"></div>
            <div id="operationDiv" class="layout-right">
                <button class="btnClass" @click="dcsDataShow">DCS数据</button>
                <button class="btnClass" @click="alarmDataShow">设备告警</button>
                <button class="btnClass" @click="riskDataShow">风险预警</button>
                <button class="btnClass" @click="damageDataShow">损伤分布</button>
            </div>
        </div>
    </div>
    <div>
        <button @click="exportData" style="margin: 8px;">导出数据</button>
        <button @click="toggleEditMode" style="margin: 8px;">切换编辑/预览模式</button>
        <button @click="APItest" style="margin: 8px;">测试API按钮</button>
        <button @click="horizontalFlip" style="margin: 8px;">水平翻转选中节点</button>
        <button @click="verticalFlip" style="margin: 8px;">垂直翻转选中节点</button>
    </div>

    <el-dialog v-model="dialogVisible" title="给当前节点添加端口/标定点">
        <div>
            <el-switch v-model="changeModel" @change="toggleDivs">
            </el-switch>
            <br>
            <div v-if="changeModel">
                <button @click="addPort('top')" style="margin-right: 8px;">添加上端口</button>
                <button @click="addPort('bottom')" style="margin-right: 8px;">添加下端口</button>
                <button @click="addPort('left')" style="margin-right: 8px;">添加左端口</button>
                <button @click="addPort('right')" style="margin-right: 8px;">添加右端口</button>
                <button style="margin-left: 280px" @click="addDataPanel">创建数据面板</button>
            </div>
            <div v-else>
                <button @click="addMark()">添加标定点</button>
            </div>
        </div>
    </el-dialog>

    <el-dialog v-model="pipeDialogVisible" title="添加管道">
        <button @click="addPipe">添加管道</button>
    </el-dialog>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import go, { Geometry } from 'gojs';
import { PortShiftingTool } from './extensions/PortShiftingTool';
import { ResizeMultipleTool } from './extensions/ResizeMultipleTool';
// import { LinkLabelDraggingTool } from './extensions/LinkLabelDraggingTools';
import { NodeLabelDraggingTool } from './extensions/NodeLabelDraggingTool';
import { GuidedDraggingTool } from './extensions/GuidedDraggingTool';
import { RotateMultipleTool } from './extensions/RotateMultipleTool';
import { ElMessage } from 'element-plus';
import { LinkLabelOnPathDraggingTool } from './extensions/LinkLabelOnPathDraggingTool';

const $ = go.GraphObject.make;
var myDiagram: any;
const dialogVisible = ref(false)
const pipeDialogVisible = ref(false)
const changeModel = ref(true)

// 计算偏移量变量
const dragStartOffsetX = ref()
const dragStartOffsetY = ref()

// 控制展示面板内容展示和隐藏的参数
const showDcsVisible = ref(true)
const showAlarmVisible = ref(true)
const showRiskVisible = ref(true)
const showDamageVisible = ref(true)

// 端口模板
const portPanel = $(go.Panel,
    {
        portId: "Top",
        fromSpot: go.Spot.Top,
        toSpot: go.Spot.Top,
        fromLinkable: true,
        toLinkable: true,
        cursor: 'pointer',
        alignment: go.Spot.Top,
        visible: true,
        contextMenu:
        $("ContextMenu",
            $("ContextMenuButton",
                $(go.TextBlock, "Remove Port", { font: "bold 12px sans-serif", width: 100, textAlign: "center" }),
                {
                    click: (e: any, obj: any) => removePort(obj.part.adornedObject),
                    "ButtonBorder.fill": "white",
                    "_buttonFillOver": "skyblue"
                }
            )
        ),
    },
    new go.Binding('portId', 'portId'),
    new go.Binding('alignment', 'portKey', (portKey: string) => {
        switch(portKey) {
            case "top": return go.Spot.Top;
            case "bottom": return go.Spot.Bottom;
            case "left": return go.Spot.Left;
            case "right": return go.Spot.Right;
            default: return go.Spot.Top;
        }
    }),
    new go.Binding('fromSpot', 'portKey', (portKey: string) => {
        switch(portKey) {
            case "top": return go.Spot.Top;
            case "bottom": return go.Spot.Bottom;
            case "left": return go.Spot.Left;
            case "right": return go.Spot.Right;
            default: return go.Spot.Top;
        }
    }),
    new go.Binding('toSpot', 'portKey', (portKey: string) => {
        switch(portKey) {
            case "top": return go.Spot.Top;
            case "bottom": return go.Spot.Bottom;
            case "left": return go.Spot.Left;
            case "right": return go.Spot.Right;
            default: return go.Spot.Top;
        }
    }),
    $(go.Shape, 'Rectangle',
        {
            strokeWidth: 1,
            desiredSize: new go.Size(6, 6),
        },
        new go.Binding('visible', 'visible'),
    )
)

// 标定点模板
const markPanel = $(go.Panel,
    {
        portId: "mark",
        cursor: 'pointer',
        alignment: new go.Spot(0.5, 0.3),
        contextMenu:
        $("ContextMenu",
            $("ContextMenuButton",
                $(go.TextBlock, "Remove Mark", { font: "bold 12px sans-serif", width: 100, textAlign: "center" }),
                {
                    click: (e: any, obj: any) => removeMark(obj.part.adornedObject),
                    "ButtonBorder.fill": "white",
                    "_buttonFillOver": "skyblue"
                }
            )
        ),
    },
    new go.Binding('portId', 'markId'),
    $(go.Shape, 'Rectangle',
        {
            strokeWidth: 1,
            desiredSize: new go.Size(6, 6),
            fill: "red"
        },
    )
)

var zhaChiGeometry = go.Geometry.parse("XFM88 77.8 0 77.8 0 53.8 88 53.8 136.6 0 181.4 0 181.4 35.3 157.5 35.3 157.5 24.5 136.6 24.5z XM 86.8 70.1 L 141.7 10.2 XM 82.8 66.1 L 137.1 6.4 XM142 8.8B 0 360 139 8.8 3 3 XM87 68.8B 0 360 84 68.8 3 3");

// 切换添加端口/标定点的形式
function toggleDivs(value: boolean) {
    changeModel.value = value;
}

function initDiagram() {
    myDiagram = $(go.Diagram, "diagramDiv", {
        "undoManager.isEnabled": true,
        'grid.visible': true,  // 画布上面是否出现网格
        "grid.gridCellSize": new go.Size(5, 5),  // 设置背景网格的大小
        "toolManager.mouseWheelBehavior": go.WheelMode.Zoom,
        // contentAlignment: go.Spot.Center, // 元素位置移动后始终处于在画布正中间
        resizingTool: new ResizeMultipleTool(),  // 自定义ResizeMultipleTool()方法来设置元素大小的缩放
        draggingTool: new GuidedDraggingTool(),  // 使用节点对齐辅助
        // 设置辅助对齐的线条的样式
        "draggingTool.horizontalGuidelineColor": "blue",  // 水平两侧的辅助线条为蓝色
        "draggingTool.verticalGuidelineColor": "blue",    // 垂直两侧的辅助线条为蓝色
        "draggingTool.centerGuidelineColor": "green",     // 节点中心的水平和垂直对齐的辅助线条为绿色
        "draggingTool.guidelineWidth": 1,    // 设置辅助对齐的线条的粗细
        // 旋转节点
        rotatingTool: new RotateMultipleTool(),
    });

    myDiagram.toolManager.mouseMoveTools.insertAt(0, new PortShiftingTool());  // 设置端口移动
    //myDiagram.toolManager.mouseMoveTools.insertAt(0, new LinkLabelDraggingTool());  // 设置链接上的文本可以移动
    myDiagram.toolManager.mouseMoveTools.insertAt(0, new LinkLabelOnPathDraggingTool());  // 设置连接上的文本只能沿着连接移动
    myDiagram.toolManager.mouseMoveTools.insertAt(0, new NodeLabelDraggingTool());  // 设置节点上的文本可以移动

    myDiagram.nodeTemplate =
        $(go.Node, "Spot", 
            { 
                resizable: true,
                rotatable: true
            },
            new go.Binding("location", "loc"),
            new go.Binding("desiredSize", "size", go.Size.parse).makeTwoWay(go.Size.stringify),  // 进行元素位置信息的绑定
            // 端口模板
            new go.Binding('itemArray', 'portArray'), { 
                itemTemplate: portPanel,
            },
            $(go.Panel, 'Spot',
            // 标定点模板
            new go.Binding('itemArray', 'markArray'), { 
                itemTemplate: markPanel
            },
            $(go.Panel, 'Spot',
                $(go.Shape, "RoundedRectangle", 
                { 
                    fill: "white",
                    strokeWidth: 0
                },
                new go.Binding("fill", "color"),
                ),
                $(go.TextBlock,
                    { 
                        margin: 10, 
                        textAlign: 'center', 
                        font: 'bold 14px Segoe UI,sans-serif', 
                        stroke: '#484848', 
                        editable: true,
                        _isNodeLabel: true,
                        cursor: "move"
                    },
                    new go.Binding('text', 'key').makeTwoWay(),
                ),
                {
                    toolTip:  // 定义节点工具提示
                        $("ToolTip",
                            $(go.TextBlock, { margin: 4 },
                                new go.Binding("text", "key"))  // 绑定节点的颜色信息
                        )
                },
                {
                    contextMenu:   // 为每个节点定义上下文菜单
                    $("ContextMenu",  
                        $("ContextMenuButton",
                            $(go.TextBlock, "Cut", { font: "bold 12px sans-serif", width: 100, textAlign: "center" }),
                            { 
                                click: (e: any) => e.diagram.commandHandler.cutSelection(),
                                "ButtonBorder.fill": "white",
                                "_buttonFillOver": "skyblue",
                            }
                        ),
                        $("ContextMenuButton",
                            $(go.TextBlock, "Copy", { font: "bold 12px sans-serif", width: 100, textAlign: "center" }),
                            { 
                                click: (e: any) => e.diagram.commandHandler.copySelection(),
                                "ButtonBorder.fill": "white",
                                "_buttonFillOver": "skyblue",
                            }
                        )
                    )
                },
                {
                    doubleClick : function(){   // 在节点中鼠标左键双击打开添加节点端口弹出框
                        dialogVisible.value = true;
                    }
                }
            )
            ),
        ),
    
    // SVG图片节点模板
    myDiagram.nodeTemplateMap.add('zhaChi',
    $(go.Node, "Spot", 
        {
            resizable: true,
            rotatable: true
        },
        new go.Binding("location", "loc"),
        new go.Binding("desiredSize", "size", go.Size.parse).makeTwoWay(go.Size.stringify),  // 进行元素位置信息的绑定
        new go.Binding('itemArray', 'portArray'), { 
            itemTemplate: portPanel,
        },
        $(go.Panel, 'Spot',
        // 标定点模板
        new go.Binding('itemArray', 'markArray'), { 
            itemTemplate: markPanel
        },
        $(go.Panel, 'Spot',
        $(go.Shape, "RoundedRectangle", 
            { 
                geometry: zhaChiGeometry,
                stroke: "black",
                fill: "white",
                strokeWidth: 1.5
            },
            new go.Binding('geometry', 'geometry').makeTwoWay(),
            // new go.Binding('geometry', '', (data)=>{
            //     let geometry = new go.Geometry.parse()
            //     geometry.scale(data)
            //     return geometry
            // })
        ),
        $(go.TextBlock,
            { 
                margin: 10, 
                textAlign: 'center', 
                font: 'bold 14px Segoe UI,sans-serif', 
                stroke: '#484848', 
                editable: true,
                _isNodeLabel: true,
                cursor: "move",
            },
            new go.Binding('text', 'key').makeTwoWay(),
        ),
        {
            toolTip:  // 定义节点工具提示
                $("ToolTip",
                    $(go.TextBlock, { margin: 4 },
                        new go.Binding("text", "key"))  // 绑定节点的颜色信息
                )
        },
        {
            contextMenu:   // 为每个节点定义上下文菜单
            $("ContextMenu",  
                $("ContextMenuButton",
                    $(go.TextBlock, "Cut", { font: "bold 12px sans-serif", width: 100, textAlign: "center" }),
                    { 
                        click: (e: any) => e.diagram.commandHandler.cutSelection(),
                        "ButtonBorder.fill": "white",
                        "_buttonFillOver": "skyblue",
                    }
                ),
                $("ContextMenuButton",
                    $(go.TextBlock, "Copy", { font: "bold 12px sans-serif", width: 100, textAlign: "center" }),
                    { 
                        click: (e: any) => e.diagram.commandHandler.copySelection(),
                        "ButtonBorder.fill": "white",
                        "_buttonFillOver": "skyblue",
                    }
                )
            )
        },
        {
            doubleClick : function(){   // 在节点中鼠标左键双击打开添加节点端口弹出框
                dialogVisible.value = true;
            }
        }
        )),
        )
    );

    // 管道模板
    myDiagram.nodeTemplateMap.add('pipe',
        $(go.Node, 'Spot',
            {
                resizable: true,
                rotatable: true,
                cursor: 'move',
                segmentIndex: NaN,
                segmentFraction: 0.5,
                visible: true,
                _isLinkLabel: true,
                layerName: 'Foreground'
            },
            new go.Binding("location", "loc"),
            new go.Binding("desiredSize", "size", go.Size.parse).makeTwoWay(go.Size.stringify), 
            new go.Binding('itemArray', 'portArray'), { 
                itemTemplate: portPanel,
            },
            $(go.Panel, 'Spot',
            // 标定点模板
            new go.Binding('itemArray', 'markArray'), { 
                itemTemplate: markPanel
            },
            $(go.Panel, 'Spot',
                $(go.Shape, "RoundedRectangle", 
                    { 
                        geometry: go.Geometry.parse("XF M 0 0 L 30 0 L 30 30 L 0 30 Z"),
                        stroke: "black",
                        fill: "gray",
                        strokeWidth: 1.5,
                        width: 30,
                        height: 30
                    },
                    new go.Binding('fill', 'color'),
                ),
                $(go.TextBlock,
                    { 
                        margin: 10, 
                        textAlign: 'center', 
                        font: 'bold 14px Segoe UI,sans-serif', 
                        stroke: '#484848', 
                        editable: true,
                        _isNodeLabel: true,
                        cursor: "move" 
                    },
                    // new go.Binding('text', 'key').makeTwoWay(),
                ),
                {
                    toolTip:  // 定义节点工具提示
                        $("ToolTip",
                            $(go.TextBlock, { margin: 4 },
                                new go.Binding("text", "key"))  // 绑定节点的颜色信息
                        )
                },
                {
                    doubleClick : function(){   // 在节点中鼠标左键双击打开添加节点端口弹出框
                        dialogVisible.value = true;
                    }
                }
              )
            )
        )
    );

    // 数据展示面板模板
    myDiagram.nodeTemplateMap.add('infoPanel',
        $(go.Node, "Spot",
        {
                resizable: true,
                rotatable: true,
                cursor: 'move',
                _isLinkLabel: true,
            },
            new go.Binding("location", "loc"),
            new go.Binding("desiredSize", "size", go.Size.parse).makeTwoWay(go.Size.stringify), 
            new go.Binding('itemArray', 'portArray'), { 
                itemTemplate: portPanel,
            },
            $(go.Panel, "Spot",
                $(go.Panel, "Auto",
                    $(go.Shape, { fill: '#f4f4f4', stroke: 'black', strokeWidth: 1 }),  // 设置最外层边框
                    $(go.Panel, "Table",
                        // 设置内部边框
                        $(go.RowColumnDefinition, { row: 0, separatorStroke: 'black' }),
                        $(go.RowColumnDefinition, { row: 1, separatorStroke: 'black' }),
                        $(go.RowColumnDefinition, { row: 2, separatorStroke: 'black' }),
                        $(go.RowColumnDefinition, { row: 3, separatorStroke: 'black' }),
                        $(go.Panel, "Table",
                            $(go.TextBlock, 
                                { 
                                    stroke: 'black', 
                                    margin: 4, 
                                    row: 0, 
                                    column: 0, 
                                },
                                new go.Binding('text','key')
                            ),
                            // 报警标志样式模板
                            $(go.Shape, "Triangle", 
                                { 
                                    desiredSize: new go.Size(20, 20), 
                                    stroke: 'black', 
                                    row: 0, 
                                    column: 1, 
                                    margin: 4 
                                },
                                {
                                    toolTip:  // 定义节点工具提示
                                        $("ToolTip",
                                            $(go.TextBlock, { margin: 4 },
                                                new go.Binding("text", "riskData"))  // 绑定设备的风险信息
                                        )
                                },
                                new go.Binding('fill', 'color'),
                                new go.Binding('visible', '', (data: any, obj: any) => {
                                    const nodeData = obj.part.data;
                                    return nodeData.riskVisible !== false;
                                })
                            )
                        ),
                        // DCS面板
                        $(go.Panel, "Table", { row: 1, column: 0 },
                            { 
                                defaultColumnSeparatorStroke: 'black', 
                                defaultRowSeparatorStroke: 'black' 
                            },
                            new go.Binding('itemArray', 'DCSArray'), 
                            {
                                itemTemplate: $(go.Panel, "TableRow",
                                    // 参数名模板
                                    $(go.TextBlock, 
                                        { 
                                            stroke: 'black', 
                                            margin: 4,
                                            width: 40,
                                            textAlign: "center"
                                        },
                                        new go.Binding('text', 'name')
                                    ),
                                    // value模板
                                    $(go.TextBlock, 
                                        { 
                                            stroke: 'black',   
                                            column: 1, 
                                            margin: 4,
                                            width: 40,
                                            textAlign: "center"
                                        },
                                        new go.Binding('text', 'value')
                                    ),
                                    // 单位模板
                                    $(go.TextBlock, 
                                        {
                                            stroke: 'black', 
                                            column: 2, 
                                            margin: 4,
                                            width: 40,
                                            textAlign: "center"
                                        },
                                        new go.Binding('text', 'unit')
                                    ),
                                    new go.Binding('visible', '', (data: any, obj: any) => {
                                        const nodeData = obj.part.data;
                                        return nodeData.dcsVisible !== false;
                                    })
                                )
                            }
                        ),
                        // 告警数据
                        // $(go.Panel, "Table", { row: 2, column: 0 },
                        //     {
                        //         defaultColumnSeparatorStroke: 'black',
                        //         defaultRowSeparatorStroke: 'black'
                        //     },
                        //     new go.Binding('itemArray', 'alarmArray'),
                        //     {
                        //         itemTemplate: $(go.Panel, "TableColumn",
                        //             $(go.TextBlock,
                        //                 {
                        //                     stroke: 'black',
                        //                     margin: 4
                        //                 },
                        //                 new go.Binding('text', 'alarmName')
                        //             ),
                        //             new go.Binding('visible', '', (data: any, obj: any) => {
                        //                 const nodeData = obj.part.data;
                        //                 return nodeData.alarmVisible !== false;
                        //             })
                        //         )
                        //     }
                        // ),
                        // 损伤数据
                        $(go.Panel, "Table", { row: 3, column: 0 },
                            { 
                                defaultColumnSeparatorStroke: 'black', 
                                defaultRowSeparatorStroke: 'black' 
                            },
                            new go.Binding('itemArray', 'damageArray'), 
                            {
                                itemTemplate: $(go.Panel, "TableRow",
                                    // 损伤名模板
                                    $(go.TextBlock, 
                                        { 
                                            stroke: 'black', 
                                            margin: 4,
                                        },
                                        new go.Binding('text', 'damageName')
                                    ),
                                    // value模板
                                    $(go.TextBlock, 
                                        { 
                                            stroke: 'black',   
                                            column: 1, 
                                            margin: 4,
                                        },
                                        new go.Binding('text', 'damageValue')
                                    ),
                                    new go.Binding('visible', '', (data: any, obj: any) => {
                                        const nodeData = obj.part.data;
                                        return nodeData.damageVisible !== false;
                                    })
                                )
                            }
                        ),
                    )
                )
            )
        )
    );

    // 节点间的连线模板
    myDiagram.linkTemplate =
    $(go.Link,
        {
            routing: go.Routing.Orthogonal, 
            curve: go.Curve.JumpGap,
            corner: 10,
            adjusting: go.LinkAdjusting.End, 
            reshapable: true,  // 设置连接线的形态是否可以被修改
            resegmentable: true,  // 设置连接线可以分段的编辑
            selectable: true,
            toEndSegmentLength: 20
        },
        $(go.Shape,  // 链接线的样式
            { 
                strokeWidth: 1.5
            }
        ),
        $(go.Shape,  // 箭头的样式
            { 
                toArrow: "standard", 
                stroke: null 
            }
        ),
        {
            doubleClick : function(){   // 在节点中鼠标左键双击打开添加管道弹出框
                pipeDialogVisible.value = true;
            }
        },
    );

    // 数据面板的连线模板
    myDiagram.linkTemplateMap.add('infoPanelLink',
        $(go.Link,
            { 
                selectable: true,
                resegmentable: true,
                routing: go.Routing.Orthogonal, 
                curve: go.Curve.JumpGap, 
                toShortLength: 2, 
                adjusting: go.LinkAdjusting.End 
            },
            new go.Binding("points"),
            $(go.Shape, { isPanelMain: true, strokeWidth: 2, stroke: 'gray' }),
            $(go.Shape, { isPanelMain: true, strokeWidth: 2, stroke: 'black', name: "FLOW", strokeDashArray: [10, 10] }),
        )      
    );
    
    // 画布提示工具函数
    function diagramInfo(model: any) {
        return "Model:\n" + model.nodeDataArray.length + " nodes, " + model.linkDataArray.length + " links";
    };

    // 当未覆盖任何节点时，提供图表背景的工具提示
    myDiagram.toolTip =
    $("ToolTip",
        $(go.TextBlock, { margin: 4 },
        new go.Binding("text", "", diagramInfo)) // 绑定函数转换器显示相关的信息
    );

    myDiagram.contextMenu =
    $("ContextMenu",
        // 创建新节点上下文按钮
        $("ContextMenuButton",
        $(go.TextBlock, "New Node", { font: "bold 12px sans-serif", width: 100, textAlign: "center" }),
        { 
            click: function(e: any) {
                e.diagram.commit(function(d: any) {
                    var data = {
                        key: "new node",
                        color: 'aqua',
                        portArray: [],
                        markArray: [],
                        category: ""
                    };
                    d.model.addNodeData(data);
                    var part = d.findPartForData(data);
                    // 在ContextMenuTool中设置保存mouseDownPoint的位置
                    // 节点创建的位置就是鼠标右键的位置
                    if(part){
                        part.location = d.toolManager.contextMenuTool.mouseDownPoint; 
                    }
                    }, 'new node');
                },
                "ButtonBorder.fill": "white",
                "_buttonFillOver": "skyblue",
            }
        ),
        $("ContextMenuButton",
            $(go.TextBlock, "Paste", { font: "bold 12px sans-serif", width: 100, textAlign: "center" }),
            { 
                click: (e: any) => e.diagram.commandHandler.pasteSelection(e.diagram.toolManager.contextMenuTool.mouseDownPoint),
                "ButtonBorder.fill": "white",
                "_buttonFillOver": "skyblue",
            }
        ),
        // 撤销按钮
        $("ContextMenuButton",
        $(go.TextBlock, "Undo", { font: "bold 12px sans-serif", width: 100, textAlign: "center" }),
        { 
            click: function(e: any) { e.diagram.commandHandler.undo(); },
            "ButtonBorder.fill": "white",
            "_buttonFillOver": "skyblue",
        },
        new go.Binding("visible", "", function(o: any) {  // 根据是否有可撤销的操作来决定是否可见
            if (o && o.diagram) {
                return o.diagram.commandHandler.canUndo();  // 可以撤销返回true，否则返回false
            }
            return false;
        }).ofObject()),
        // 重做按钮
        $("ContextMenuButton",
        $(go.TextBlock, "Redo", { font: "bold 12px sans-serif", width: 100, textAlign: "center" }),
        { 
            click: function(e: any) { e.diagram.commandHandler.redo(); },
            "ButtonBorder.fill": "white",
            "_buttonFillOver": "skyblue",
        },
        new go.Binding("visible", "", function(o: any) {   // 根据是否有可重做的操作来决定是否可见
            if (o && o.diagram) {
                return o.diagram.commandHandler.canRedo();  // 可以重做返回true，否则返回false
            }
            return false;
        }).ofObject())
    );

    // 如果以信息面板端口为终点/起点的连接线，使用infoPanelLink类型的连接线
    myDiagram.addDiagramListener("LinkDrawn", function(e: any) {
    var link = e.subject;
    var fromNode = link.fromNode;
    var toNode = link.toNode;
    // 检查连接的起点或终点是否是信息面板
    if ((fromNode && fromNode.category === "infoPanel") || (toNode && toNode.category === "infoPanel")) {
        // 设置连接的类别为 infoPanelLink
        myDiagram.model.set(link.data, "LinkCategory", "infoPanelLink");
    }
    });

    const nodeDataArray = [
        { key: "add1", color: "lightyellow", loc: new go.Point(-150, 200), portArray: [{portId: "top0", portKey: "top"}, {portId: "left0", portKey: "left"}, {portId: "right0", portKey: "right"}, {portId: "bottom0", portKey: "bottom"}], markArray: [] },
        { key: "add2", color: "lightblue", loc: new go.Point(100, 50), category: "zhaChi", portArray: [{portId: "bottom0", portKey: "bottom"}], markArray: [] },
        { key: "add3", color: "lightblue", loc: new go.Point(300, 150), category: "zhaChi", portArray: [{portId: "bottom0", portKey: "bottom"}], markArray: [] },
        { key: "pipe1", color: "gray", loc: new go.Point(0, 100), category: "pipe", portArray: [{portId: "top0", portKey: "top"}], markArray: [{portId: "mark0"}]},
        { key: "pipe1信息面板", color: "red", loc: new go.Point(-80, -120), portArray: [{portId: "top0", portKey: "top"}, {portId: "left0", portKey: "left"}, {portId: "right0", portKey: "right"}, {portId: "bottom0", portKey: "bottom"}], DCSArray: [{name: "流速", value: "20", unit: "m/s"}, {name: "温度", value: "30", unit: "℃"}], damageArray: [{damageName: "盐酸腐蚀", damageValue: "100%"}], alarmArray: [{alarmName: "警报"}], riskData: "高风险", category: "infoPanel"}
    ];
    const linkDataArray = [
        { from: "add1", fromPort: "top0", to: "add2", toPort: "bottom0", labelKeys: ["pipe1"] },
        { from: "add1", fromPort: "bottom0", to: "add3", toPort: "bottom0" },
        { from: "pipe1信息面板", fromPort: "bottom0", to: "pipe1", toPort: "top0", LinkCategory: "infoPanelLink"}
    ];

    myDiagram.model =
        $(go.GraphLinksModel,
            {
                linkFromPortIdProperty: "fromPort",
                linkToPortIdProperty: "toPort",
                linkLabelKeysProperty: "labelKeys",
                nodeDataArray: nodeDataArray,
                linkDataArray: linkDataArray
            }
        );

    myDiagram.model.linkCategoryProperty = "LinkCategory";
}

// 导出画布中的节点和连线数据
function exportData() {
    if (myDiagram) {
        console.log(myDiagram.model.toJson());
    }
}

// 获取拖动开始时的偏移量
function dragstart(event: any){
    const target = event.target;
    dragStartOffsetX.value = event.offsetX - target.clientWidth / 2;
    dragStartOffsetY.value = event.offsetY - target.clientHeight / 2;

    // 设置拖动数据
    if (target.id === "svg_zhaChi") {
        event.dataTransfer.setData("node-type", "zhaChi");
    } else if (target.id === "html") {
        event.dataTransfer.setData("node-type", "html");
    } else if (target.id === "pipe") {
        event.dataTransfer.setData("node-type", "pipe");
    }
}

// html元素拖动到画布中
function drop(event: any) {
    event.preventDefault();  // 不要执行浏览器的默认操作，执行下面自定义的函数方法
    const target = event.target;  // 指向事件触发的原始元素
    // 获取像素比率
    const pixelRatio = myDiagram.computePixelRatio();
    if (!(target instanceof HTMLCanvasElement)) return;
    // 获取目标元素的边界框
    const bbox = target.getBoundingClientRect();
    let bbw = bbox.width;
    if (bbw === 0) bbw = 0.001;
    let bbh = bbox.height;
    if (bbh === 0) bbh = 0.001;
    // 计算鼠标在画布上的位置
    const mx = event.clientX - bbox.left * (target.width / pixelRatio / bbw);
    const my = event.clientY - bbox.top * (target.height / pixelRatio / bbh);
    const point = myDiagram.transformViewToDoc(new go.Point(mx - dragStartOffsetX.value, my - dragStartOffsetY.value));
    // 开始一个新的事务
    myDiagram.startTransaction('new node');
    // 获取拖动数据
    let nodeType = event.dataTransfer.getData("node-type");
    let category = "";
    let color = 'aqua';
    let key = "html元素";
    if (nodeType === "zhaChi") {
        category = "zhaChi";
        key = "渣池";
    }
    if (nodeType === "pipe"){
        category = "pipe";
        color = 'gray';
        key = "30x30 管道"
    }
    const newData = {
        key: key,
        color: color,
        loc: new go.Point(point.x, point.y),
        portArray: [],
        markArray: [],
        category: category
    };
    myDiagram.model.addNodeData(newData);
    myDiagram.commitTransaction('new node');
}

// 添加端口
function addPort(side: string) {
    myDiagram.startTransaction('addPort');
    myDiagram.selection.each((node: any) => {
      // 跳过任何被选定的连接
      if (!(node instanceof go.Node)) return;
      // 计算下一个可用的索引
      let i = 0;
      // 从小到大遍历索引i，获取一个可以使用的索引（没有被占用）
      while (node.findPort(side + i.toString()) !== node) i++;
      // 为新端口设置name，传入的side字符串加上可用的索引
      const name = side + i.toString();
      // 创建一个新的端口数据对象
      const newportdata = {
        portId: name,
        portKey: side
      };
      // 获取要修改的端口数据的数组，索引的属性为portArray
      const arr = node.data.portArray;
      if (arr) {
        // 其添加到端口数据数组中
        myDiagram.model.insertArrayItem(arr, -1, newportdata);
      }
    });
    myDiagram.commitTransaction('addPort');
}

// 删除端口
function removePort(port: any) {
    myDiagram.startTransaction('removePort');
    // console.log(port.portId);  // 如top0
    const pid = port.portId;
    const arr = port.panel.itemArray;
    for (let i = 0; i < arr.length; i++) {
      if (arr[i].portId === pid) {
        myDiagram.model.removeArrayItem(arr, i);  // 删除数组中的项
        break;
      }
    }
    myDiagram.commitTransaction('removePort');
}

// 添加标定点
function addMark() {
    myDiagram.startTransaction('addMark');
    myDiagram.selection.each((node: any) => {
        if (!(node instanceof go.Node)) return;
        let i = 0;
        while (node.findPort("mark" + i.toString()) !== node) i++;
        const name = "mark" + i.toString();
        const newMarkData = {
            markId: name
        };
        const arr = node.data.markArray;
        if (arr) {
            myDiagram.model.insertArrayItem(arr, -1, newMarkData);
        }
    });
    myDiagram.commitTransaction('addMark');
}

// 删除标定点
function removeMark(mark: any) {
    myDiagram.startTransaction('removeMark');
    const markId = mark.portId;
    const arr = mark.panel.itemArray;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i].markId === markId) {
            myDiagram.model.removeArrayItem(arr, i);
            break;
        }
    }
    myDiagram.commitTransaction('removeMark');
}

// 设置一开始画布为编辑模式
const isEditMode = ref(true)

// 切换编辑和预览模式
function toggleEditMode() {
    myDiagram.startTransaction("changeModel");
    isEditMode.value = !isEditMode.value;
    if(isEditMode.value){
        ElMessage('编辑模式')
    } else {
        ElMessage({
            message: '预览模式',
            type: 'success',
        })
    }
    if (myDiagram) {
        myDiagram.isReadOnly = !isEditMode.value;
        myDiagram.allowEdit = isEditMode.value;

        // 隐藏所有的节点端口
        myDiagram.nodes.each((node: any) => {
            node.ports.each((port: any) => {
                myDiagram.model.setDataProperty(port.data, 'visible', isEditMode.value);
            });
        });
    }
    myDiagram.commitTransaction("changeModel");
}

// DCS数据在展示面板中的显示/隐藏
function dcsDataShow() {
    myDiagram.startTransaction("changeDcsShowModel");
    showDcsVisible.value = !showDcsVisible.value;
    if(myDiagram){
        myDiagram.nodes.each((node: go.Node) => {
            myDiagram.model.setDataProperty(node.data, 'dcsVisible', showDcsVisible.value)
        })
    }
    myDiagram.commitTransaction("changeDcsShowModel");
}

// 告警数据在展示面板中的显示/隐藏
function alarmDataShow() {
    myDiagram.startTransaction("changeAlarmShowModel");
    showAlarmVisible.value = !showAlarmVisible.value;
    if(myDiagram){
        myDiagram.nodes.each((node: go.Node) => {
            myDiagram.model.setDataProperty(node.data, 'alarmVisible', showAlarmVisible.value)
        })
    }
    myDiagram.commitTransaction("changeAlarmShowModel");
}

// 风险数据在展示面板中的显示/隐藏
function riskDataShow(){
    myDiagram.startTransaction("changeRiskShowModel");
    showRiskVisible.value = !showRiskVisible.value;
    if(myDiagram){
        myDiagram.nodes.each((node: go.Node) => {
            myDiagram.model.setDataProperty(node.data, 'riskVisible', showRiskVisible.value)
        })
    }
    myDiagram.commitTransaction("changeRiskShowModel");
}

// 损伤数据在展示面板中的显示/隐藏
function damageDataShow() {
    myDiagram.startTransaction("changeDamageShowModel");
    showDamageVisible.value = !showDamageVisible.value;
    if(myDiagram){
        myDiagram.nodes.each((node: go.Node) => {
            myDiagram.model.setDataProperty(node.data, 'damageVisible', showDamageVisible.value)
        })
    }
    myDiagram.commitTransaction("changeDamageShowModel");
}

// 在连接线上添加管道
function addPipe() {
    myDiagram.startTransaction("addPipeToLinks");
    myDiagram.selection.each(function(link: any) {
        if (link instanceof go.Link) 
        {
            var newPipeNode = 
            {
                key: "newPipe",
                color: 'gray',
                category: "pipe",
                portArray: [],
                markArray: []
            };
            // 添加节点到节点数据模型中
            myDiagram.model.addNodeData(newPipeNode);

            // 确保link.data有linkLabels属性
            if (!link.data.linkLabels) {
                link.data.linkLabels = [];
            }
            // 向连接中添加标签键，将新节点的唯一标识符（key数据）添加到连接线的labelKeys属性中，使节点显示在连接线上
            myDiagram.model.addLabelKeyForLinkData(link.data, newPipeNode.key)
        }
    });
    myDiagram.commitTransaction("addPipeToLinks");
}

// 创建设备的数据面板
function addDataPanel(){
    myDiagram.startTransaction("addDataPanel");
    myDiagram.selection.each((node: any) => {
        if (!(node instanceof go.Node)) return;
        const newDataPanel = 
        { 
            key: `${node.data.key}信息面板`, 
            color: "red", 
            portArray: [{portId: "top0", portKey: "top"}, {portId: "left0", portKey: "left"}, {portId: "right0", portKey: "right"}, {portId: "bottom0", portKey: "bottom"}], 
            DCSArray: [{name: "流速", value: "20", unit: "m/s"}, {name: "温度", value: "30", unit: "℃"}], 
            damageArray: [{damageName: "盐酸腐蚀", damageValue: "100%"}], 
            alarmArray: [{alarmName: "警报"}], 
            riskData: "高风险", 
            category: "infoPanel"
        }
        myDiagram.model.addNodeData(newDataPanel);
    });
    myDiagram.commitTransaction("addDataPanel");
}

function APItest(){
    const linkData = myDiagram.model.linkDataArray[0];
    myDiagram.model.setLabelKeysForLinkData(linkData, ['pipe1','add3']);
}

// svg节点进行水平翻转
function horizontalFlip() {
    myDiagram.startTransaction('horizontalFlip');
    myDiagram.selection.each((node: any) => {
        if (!(node instanceof go.Node)) return;

        // 获取节点翻转标志
        var isHorizontalFlipped = node.data.isHorizontalFlipped || false;
        var isVerticalFlipped = node.data.isVerticalFlipped || false;
        
        var zhaChiGeometrySample = go.Geometry.parse("XFM88 77.8 0 77.8 0 53.8 88 53.8 136.6 0 181.4 0 181.4 35.3 157.5 35.3 157.5 24.5 136.6 24.5z XM 86.8 70.1 L 141.7 10.2 XM 82.8 66.1 L 137.1 6.4 XM142 8.8B 0 360 139 8.8 3 3 XM87 68.8B 0 360 84 68.8 3 3");
        // 根据翻转标志计算当前翻转状态
        var currentGeometry = zhaChiGeometrySample;
        if (isHorizontalFlipped) {
            currentGeometry = currentGeometry.scale(-1, 1);
        }
        if (isVerticalFlipped) {
            currentGeometry = currentGeometry.scale(1, -1);
        }
        // 翻转几何图形
        var flippedGeometry = currentGeometry.scale(-1, 1);
        myDiagram.model.setDataProperty(node.data, "geometry", flippedGeometry);
        myDiagram.model.setDataProperty(node.data, "isHorizontalFlipped", !isHorizontalFlipped);
    });
    myDiagram.commitTransaction('horizontalFlip');
}

// svg节点进行垂直翻转
function verticalFlip() {
    myDiagram.startTransaction('verticalFlip');
    myDiagram.selection.each((node: any) => {
        if (!(node instanceof go.Node)) return;

        // 获取节点翻转标志
        var isHorizontalFlipped = node.data.isHorizontalFlipped || false;  // 如果属性不存在则默认为false
        var isVerticalFlipped = node.data.isVerticalFlipped || false;

        var zhaChiGeometrySample = go.Geometry.parse("XFM88 77.8 0 77.8 0 53.8 88 53.8 136.6 0 181.4 0 181.4 35.3 157.5 35.3 157.5 24.5 136.6 24.5z XM 86.8 70.1 L 141.7 10.2 XM 82.8 66.1 L 137.1 6.4 XM142 8.8B 0 360 139 8.8 3 3 XM87 68.8B 0 360 84 68.8 3 3");
        // 根据翻转标志计算当前翻转状态
        var currentGeometry = zhaChiGeometrySample;
        if (isHorizontalFlipped) {
            currentGeometry = currentGeometry.scale(-1, 1);
        }
        if (isVerticalFlipped) {
            currentGeometry = currentGeometry.scale(1, -1);
        }

        // 翻转几何图形
        var flippedGeometry = currentGeometry.scale(1, -1);
        myDiagram.model.setDataProperty(node.data, "geometry", flippedGeometry);
        myDiagram.model.setDataProperty(node.data, "isVerticalFlipped", !isVerticalFlipped);
    });
    myDiagram.commitTransaction('verticalFlip');
}

onMounted(() => {
    initDiagram()
});
</script>

<style>
.common-layout {
    display: flex;
    justify-content: space-between;
}

.layout-container {
    display: flex;
    width: 100%;
}

.layout-aside {
    width: 10%;
    height: 900px;
    background-color: rgb(216, 212, 212);
}

.layout-main {
    width: 85%;
    height: 900px;
    background-color: #DAE4E4;
}

.layout-right {
    width: 5%;
    height: 900px;
}

.btnClass {
    width: 80px;
    height: 80px;
    margin: 10px;
}

.svg_class {
    width: 100px;
    height: 100px;
    background-color: white;
    /* border: 1px solid black; */
    display: flex;
    justify-content: center;
    align-items: center;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 10px;
    margin-top: 10px;
}
.pipeClass {
    margin-left: 5px;
    margin-top: 15px;
    margin-right: 5px;
    border: 1px solid #000;
}
</style>
