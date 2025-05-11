<template>
    <div id="diagramDiv" style="width: 100%; height: 900px; background-color: #DAE4E4;"></div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import go from 'gojs';

const initDiagram = () => {
    const $ = go.GraphObject.make;
    const diagram = $(go.Diagram, "diagramDiv",
        {
            "undoManager.isEnabled": true
        });

    function changeColor(e: any, obj: any) {
        diagram.commit(function(d) {
            // 获取包含单击的按钮的上下文菜单
            var contextmenu = obj.part;
            // 获取节点的绑定数据
            var nodedata = contextmenu.data;
            // 计算下一次的颜色
            var newcolor = "lightblue";
            switch (nodedata.color) {
                case "lightblue": newcolor = "lightgreen"; break;
                case "lightgreen": newcolor = "lightyellow"; break;
                case "lightyellow": newcolor = "orange"; break;
                case "orange": newcolor = "lightblue"; break;
            }
            // 修改当前节点的颜色
            // 这将评估数据绑定并记录UndoManager中的更改
            d.model.set(nodedata, "color", newcolor);
        }, "changed color");
    }

 
    diagram.nodeTemplate =
        $(go.Node, "Auto",
        $(go.Shape, "RoundedRectangle", { fill: "white" },
            new go.Binding("fill", "color")),
        $(go.TextBlock, { margin: 5 },
            new go.Binding("text", "key")),
        {
            contextMenu:   // 为每个节点定义上下文菜单
            $("ContextMenu",  
                $("ContextMenuButton",  // 上下文菜单按钮
                    $(go.TextBlock, "Change Color"),  // 设置上下文按钮的文本内容
                    { 
                        click: changeColor,  // 按钮点击事件，调用相关的函数
                        "ButtonBorder.fill": "white",  // 设置上下文按钮的颜色
                        "_buttonFillOver": "skyblue",  // 设置鼠标悬停时的颜色
                    }),
                // 在上下文菜单中添加新的上下文菜单按钮
                $("ContextMenuButton",
                    $(go.TextBlock, "new button"),
                    { 
                        click: function(e, obj) { console.log("new button clicked"); },  // 按钮点击事件
                    })
            )
        }
    );

    // 为画布背景定义上下文菜单按钮
    diagram.contextMenu =
        $("ContextMenu",
            $("ContextMenuButton",
                $(go.TextBlock, "Undo"),
                { 
                    click: function(e, obj) { e.diagram.commandHandler.undo(); } 
                },
                new go.Binding("visible", "", function(o) {   // 根据是否有可撤销的操作来决定是否可见
                    return o.diagram.commandHandler.canUndo();  // 可以撤销返回true，否则返回false
                }).ofObject()),
            $("ContextMenuButton",
                $(go.TextBlock, "Redo"),
                { 
                    click: function(e, obj) { e.diagram.commandHandler.redo(); } 
                },
                new go.Binding("visible", "", function(o) {  // 根据是否有可重做的操作来决定是否可见
                    return o.diagram.commandHandler.canRedo();  // 可以重做返回true，否则返回false
                }).ofObject()),
            // 没有绑定，上下文按钮始终可见
            $("ContextMenuButton",
                $(go.TextBlock, "New Node"),
                { 
                    click: function(e, obj) {
                        e.diagram.commit(function(d) {
                            var data = {};
                            d.model.addNodeData(data);
                            var part = d.findPartForData(data);
                            // 在ContextMenuTool中设置保存mouseDownPoint的位置
                            part.location = d.toolManager.contextMenuTool.mouseDownPoint;  // 节点创建的位置就是鼠标右键的位置
                        }, 'new node');
                    } 
                }
            )
        );

    var nodeDataArray = [
        { key: "Alpha", color: "lightyellow" },
        { key: "Beta", color: "orange" }
    ];
    var linkDataArray = [
        { from: "Alpha", to: "Beta" }
    ];
    diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
}

onMounted(() => {
    initDiagram()
});
</script>