<template>
    <div id="diagramDiv" style="width: 100%; height: 900px; background-color: #DAE4E4;"></div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import go from 'gojs';

function initDiagram() {
    var diagram = new go.Diagram("diagramDiv");
    var $ = go.GraphObject.make;

    diagram.nodeTemplate =
    $(go.Node, "Auto",
    //   new go.Binding("location", "loc"), // 进行元素位置信息的绑定
    new go.Binding("location", "loc", go.Point.parse),
      $(go.Shape, "RoundedRectangle",
        { fill: "white" },
        new go.Binding("fill", "color")),
      $(go.TextBlock,
        { margin: 5 },
        new go.Binding("text", "key"))
    );

    // var nodeDataArray = [
    //     // 对于每一个节点，分别指定其位置信息
    //     { key: "Alpha", color: "lightblue", loc: new go.Point(0, 0) },
    //     { key: "Beta", color: "pink", loc: new go.Point(100, 50) }
    // ];

    var nodeDataArray = [
        { key: "Alpha", color: "lightblue", loc: "0 0" }, 
        { key: "Beta", color: "pink", loc: "100 50" }
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