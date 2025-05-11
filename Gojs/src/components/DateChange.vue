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
      { locationSpot: go.Spot.Center },
      $(go.Shape, "RoundedRectangle",
        { // default values if the data.highlight is undefined:
          fill: "yellow", stroke: "orange", strokeWidth: 2 },
        new go.Binding("fill", "highlight", function(v) { return v ? "pink" : "lightblue"; }),
        new go.Binding("stroke", "highlight", function(v) { return v ? "red" : "blue"; }),
        new go.Binding("strokeWidth", "highlight", function(v) { return v ? 3 : 1; })),
      $(go.TextBlock,
        { margin: 5 },
        new go.Binding("text", "key"))
    );

    var nodeDataArray = [
        { key: "Alpha", highlight: true },
        { key: "Beta", highlight: false }  // just one node, and no links
    ];

    var linkDataArray = [
        { from: "Alpha", to: "Beta" }
    ]

    diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);

    function flash() {
        // 所有模型更改都应该发生在以下的事务中
        diagram.model.commit(function(m) {
            var data = m.nodeDataArray[0];  // 获取第一个节点数据
            m.set(data, "highlight", !data.highlight);   // 更改highlight属性，布尔类型的属性值取反
        }, "flash");
    }
    function loop() {
        setTimeout(function() { flash(); loop(); }, 500);  // 每0.5秒改变一次
    }
    loop();
}
onMounted(() => {
    initDiagram()
});
</script>