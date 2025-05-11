<template>
    <div id="diagramDiv" style="width: 100%; height: 900px; background-color: #DAE4E4;"></div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import go from 'gojs';

function initDiagram() {
    const $ = go.GraphObject.make;
    var myDiagram =
    $(go.Diagram, "diagramDiv",
      {
        "InitialLayoutCompleted": loadDiagramProperties,
        "toolManager.mouseWheelBehavior": go.WheelMode.Zoom,
        "clickCreatingTool.archetypeNodeData": { text: "new node" }
      });

    function loadDiagramProperties() {
        var violetbrush = $(go.Brush, "Linear", { 0.0: "Violet", 1.0: "Lavender" });

        myDiagram.add(
        $(go.Node, "Auto",
            $(go.Shape, "RoundedRectangle",
            { fill: violetbrush }),
            $(go.TextBlock, "Hello!",
            { margin: 5 })
        ));

        myDiagram.add(
        $(go.Node, "Auto",
            $(go.Shape, "Ellipse",
            { fill: violetbrush }),
            $(go.TextBlock, "Goodbye!",
            { margin: 5 })
        ));
    }
}


onMounted(() => {
    initDiagram()
});
</script>