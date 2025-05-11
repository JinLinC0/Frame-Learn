<template>
    <div id="diagramDiv" style="width: 100%; height: 900px; background-color: #DAE4E4;"></div>
    <div>
        <button @click="addNode">添加新节点</button>
        <button @click="addLink">添加链接</button>
        <button @click="exportData">导出数据</button>
    </div>
</template>
  
<script setup lang="ts">
import { onMounted } from 'vue';
import go from 'gojs';

const $ = go.GraphObject.make;
var myDiagram: any;


function initDiagram(){
    myDiagram = $(go.Diagram, "diagramDiv", {
        "toolManager.mouseWheelBehavior": go.WheelMode.Zoom,
        contentAlignment: go.Spot.Center, // 元素位置移动后始终处于在画布正中间
        'undoManager.isEnabled': true,
    });

    myDiagram.nodeTemplate =
        $(go.Node, "Auto",
            new go.Binding("location", "loc"),
            $(go.Shape, "RoundedRectangle",
                {
                    fill: "white", 
                    stroke: "black", 
                    strokeWidth: 2,
                    width: 65,
                    height: 30,
                    portId: '',
                    cursor: 'pointer',
                    fromLinkable: true,
                    fromLinkableSelfNode: true,
                    fromLinkableDuplicates: true,
                    toLinkable: true,
                    toLinkableSelfNode: true,
                    toLinkableDuplicates: true,
                },
                new go.Binding("fill", "color")
            ),
            $(go.TextBlock,
                { margin: 5 },
                new go.Binding("text", "text")
            ),
            {
                toolTip:  // 定义节点工具提示
                    $("ToolTip",
                        $(go.TextBlock, { margin: 4 },
                            new go.Binding("text", "color"))  // 绑定节点的颜色信息
                    )
            },
            {
                contextMenu:   // 为每个节点定义上下文菜单
                $("ContextMenu",  
                    $("ContextMenuButton",
                        $(go.TextBlock, "Cut"),
                        { 
                            click: (e) => e.diagram.commandHandler.cutSelection(),
                            "ButtonBorder.fill": "white",
                            "_buttonFillOver": "skyblue",
                        }
                    ),
                    $("ContextMenuButton",
                        $(go.TextBlock, "Copy"),
                        { 
                            click: (e) => e.diagram.commandHandler.copySelection(),
                            "ButtonBorder.fill": "white",
                            "_buttonFillOver": "skyblue",
                        }
                    )
                )
            }
        );
    
    myDiagram.linkTemplate =
        $(go.Link,
            {
                selectionAdorned: true, 
                fromPortId: "from", 
                toPortId: "to", 
                relinkableTo: true,  // 允许重新连接
                relinkableFrom: true, // 允许重新链接
            },
            $(go.Shape,  // 设置链接线样式
                {
                    stroke: "black",
                    strokeWidth: 2
                },
                new go.Binding("stroke", "color")
            ),
            $(go.Shape,   // 设置箭头样式
                { 
                    toArrow: "Triangle", 
                    fill: "black"
                },
                new go.Binding("fill", "color")
            )
        );

    myDiagram.groupTemplate =
        $(go.Group, "Vertical",
            $(go.Panel, "Auto",
                $(go.Shape, "RoundedRectangle",  // 围绕着占位符Placeholder
                { 
                    parameter1: 14,
                    fill: "rgba(128,128,128,0.33)",
                    portId: '',  
                    cursor: 'pointer',
                    fromLinkable: true,
                    fromLinkableSelfNode: true,
                    fromLinkableDuplicates: true,
                    toLinkable: true,
                    toLinkableSelfNode: true,
                    toLinkableDuplicates: true,
                }),
                $(go.Placeholder,    //占位符,表示所有构件的面积，
                { padding: 5})  // 添加内边距
            ),
            $(go.TextBlock,
                { alignment: go.Spot.Right, font: "Bold 12pt Sans-Serif" },
                new go.Binding("text", "text"))
            );

    // 画布提示工具函数
    function diagramInfo(model: any) {
        return "Model:\n" + model.nodeDataArray.length + " nodes, " + model.linkDataArray.length + " links";
    }

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
        $(go.TextBlock, "New Node"),
        { 
            click: function(e) {
                e.diagram.commit(function(d) {
                    var data = {};
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
            $(go.TextBlock, "Paste"),
            { 
                click: (e) => e.diagram.commandHandler.pasteSelection(e.diagram.toolManager.contextMenuTool.mouseDownPoint),
                "ButtonBorder.fill": "white",
                "_buttonFillOver": "skyblue",
            }
        ),
        // 撤销按钮
        $("ContextMenuButton",
        $(go.TextBlock, "Undo"),
        { 
            click: function(e) { e.diagram.commandHandler.undo(); },
            "ButtonBorder.fill": "white",
            "_buttonFillOver": "skyblue",
        },
        new go.Binding("visible", "", function(o) {   // 根据是否有可撤销的操作来决定是否可见
            return o.diagram.commandHandler.canUndo();  // 可以撤销返回true，否则返回false
        }).ofObject()),
        // 重做按钮
        $("ContextMenuButton",
        $(go.TextBlock, "Redo"),
        { 
            click: function(e) { e.diagram.commandHandler.redo(); },
            "ButtonBorder.fill": "white",
            "_buttonFillOver": "skyblue",
        },
        new go.Binding("visible", "", function(o) {   // 根据是否有可重做的操作来决定是否可见
            return o.diagram.commandHandler.canRedo();  // 可以重做返回true，否则返回false
        }).ofObject())
    );

    var nodeDataArray = [
        { key: 1, text: "Alpha", color: "lightblue", loc: new go.Point(0, 0)},
        { key: 2, text: "Beta" , color: "pink", loc: new go.Point(100, 0)},   
        { key: 3, text: "Gamma", color: "lightgreen", group: 4, loc: new go.Point(10, 80) },  // 在组内部
        { key: 4, text: "Omega", isGroup: true, loc: new go.Point(100, 150) },  // 设置为组
        { key: 5, text: "Delta", color: "orange", group: 4, loc: new go.Point(100, 80) }  // 在组内部
    ];
    var linkDataArray = [
        { from: 1, to: 2, color: "blue" },
        { from: 2, to: 2, color: "red" },
        { from: 3, to: 1, color: "yellow" },
        { from: 3, to: 5, color: "green" }
    ];

    myDiagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
}

function addNode() {
    if (myDiagram) {
        myDiagram.model.addNodeData({ key: 6, text: "new", color: "red", loc: new go.Point(-100, -100) });
    }
}

function addLink() {
    if (myDiagram) {
        myDiagram.model.addLinkData({ from: 2, to: 6 });
    }
}

function exportData() {
    if (myDiagram) {
        console.log(myDiagram.model.toJson());
    }
}

onMounted(() => {
    initDiagram()
});
</script>