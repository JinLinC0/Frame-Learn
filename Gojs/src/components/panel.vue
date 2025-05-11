<template>
    <div id="diagramDiv" style="width: 100%; height: 900px; background-color: #DAE4E4;"></div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import go from 'gojs';

function initDiagram() {
    var diagram = new go.Diagram("diagramDiv");
    var $ = go.GraphObject.make;
    diagram.add(
    $(go.Part, go.Panel.Position,
      { background: "lightgray" },
      $(go.TextBlock, "default, at (0,0)", { background: "lightgreen" }),
      $(go.TextBlock, "(100, 0)", { position: new go.Point(100, 0), background: "lightgreen" }),
      $(go.TextBlock, "(0, 100)", { position: new go.Point(0, 100), background: "lightgreen" }),
      $(go.TextBlock, "(55, 28)", { position: new go.Point(55, 28), background: "lightgreen" }),
      $(go.TextBlock, "(33, 70)", { position: new go.Point(33, 70), background: "lightgreen" }),
      $(go.TextBlock, "(100, 100)", { position: new go.Point(100, 100), background: "lightgreen" })
    ));
}

onMounted(() => {
    initDiagram()
});
</script>