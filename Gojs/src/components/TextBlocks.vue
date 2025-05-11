<template>
    <div id="diagramDiv" style="width: 100%; height: 900px; background-color: #DAE4E4;"></div>
</template>
  
<script setup lang="ts">
import { onMounted } from 'vue';
import go from 'gojs';

function initDiagram(){
    var $ = go.GraphObject.make;

    const myDiagram = $(go.Diagram, "diagramDiv", {
        // 配置Diagram画布配置
        //'undoManager.isEnabled': true, // 启用撤销重做功能
        //isReadOnly: true,  //只读 元素不可拖动
        contentAlignment: go.Spot.Center, // 元素位置移动后始终处于在画布正中间
        maxSelectionCount: 1,  // 最多选择一个元素
        'grid.visible': true, // 画布上面是否出现网格
        allowZoom: false, // 不允许用户改变图表的规模
    });

    myDiagram.nodeTemplate = $(go.Node, "Auto",
        $(go.Shape, "RoundedRectangle",  
        new go.Binding("fill", "color")),
        $(go.TextBlock,
        { 
            font: 'bold 32px serif',
            // stroke: '#492',
            // background: '#492',
            margin: 10,
            // width: 100,
            // height: 30,
            width: 170, height: 60, background: "lightgreen",
            textAlign: 'center',
            // alignment: go.Spot.Right,
            verticalAlignment: go.Spot.Center,
            editable: true,
        },
        new go.Binding("text", "key"))
    );

    myDiagram.model = new go.GraphLinksModel(
    [ 
    { key: "Alpha", color: "lightblue" },
    { key: "Beta", color: "orange" },
    { key: "Gamma", color: "lightgreen" },
    { key: "Delta", color: "pink" }
    ],
    [
    { from: "Alpha", to: "Beta" },
    { from: "Alpha", to: "Gamma" },
    { from: "Beta", to: "Beta" },
    { from: "Gamma", to: "Delta" },
    { from: "Delta", to: "Alpha" }
    ]);
}

onMounted(() => {
    initDiagram()
});
</script>