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
      $(go.Shape,
        { 
    		figure: "RoundedRectangle",
         	fill: "white"  // 会被后续创建的元素设置的背景颜色覆盖
		},
        new go.Binding("fill", "color")  // 后续创建的元素设置的背景颜色进行绑定
      ),
        
      $(go.TextBlock,
        { 
    		text: "hello!",  // 会被后续创建的元素设置的文本覆盖
         	margin: 5 
		},
        new go.Binding("text", "key")   // 后续创建的元素设置的文本进行绑定
      )
     );

    var nodeDataArray = [
        { key: "Hello", color: "lightblue" },
        { key: "World!", color: "orange" },
    ];
    var linkDataArray = [
        { from: "Hello", to: "World!" },
    ];
    diagram.model = new go.GraphLinksModel(nodeDataArray, linkDataArray);
}

onMounted(() => {
    initDiagram()
}); 
</script>