<template>
    <div id="diagramDiv" style="width: 100%; height: 900px; background-color: #DAE4E4;"></div>
</template>

<script setup lang="ts">
import go from 'gojs';
import { onMounted } from 'vue';

const initDiagram = () => {
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
        { key: "Alpha", color: "lightblue" },
        { key: "Beta", parent: "Alpha", color: "yellow" },  //指定父节点是哪个元素组件
        { key: "Gamma", parent: "Alpha", color: "orange" },
        { key: "Delta", parent: "Alpha", color: "lightgreen" }
    ];
    diagram.model = new go.TreeModel(nodeDataArray);


    // 查找并修改元素的颜色
    var data = diagram.model.findNodeDataForKey("Delta");
    if (data !== null) diagram.model.setDataProperty(data, "color", "red");
}

onMounted(() => {
    initDiagram()
})

</script>
