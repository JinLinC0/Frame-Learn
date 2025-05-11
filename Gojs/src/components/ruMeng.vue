<template>
    <div id="diagramDiv" style="width: 100%; height: 900px; background-color: #DAE4E4;"></div>
</template>

<script setup lang="ts">
import go from 'gojs';
import { onMounted } from 'vue';

function initDiagram(){
    var diagram = new go.Diagram("diagramDiv");
    diagram.model = new go.GraphLinksModel(
    [
        { key: "Hello" },
        { key: "World!" },
    ],

    [
        { from: "Hello", to: "World!"},
    ]
    );
}

onMounted(() => {
    initDiagram()
});
</script>