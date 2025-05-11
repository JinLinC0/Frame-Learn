<template>
    <div id="diagramDiv" style="width: 100%; height: 900px; background-color: #DAE4E4;"></div>
</template>
  
<script setup lang="ts">
import { onMounted } from 'vue';
import go from 'gojs';

function initDiagram(){
    const $ = go.GraphObject.make;  // 创建GoJS的帮助函数
    const myDiagram = $(go.Diagram, "diagramDiv", {
        // 配置Diagram画布配置
        //'undoManager.isEnabled': true, // 启用撤销重做功能
        //isReadOnly: true,  //只读 元素不可拖动
        contentAlignment: go.Spot.Center, // 元素位置移动后始终处于在画布正中间
        maxSelectionCount: 1,  // 最多选择一个元素
        'grid.visible': true, // 画布上面是否出现网格
        allowZoom: false, // 不允许用户改变图表的规模
    });

    // 创建模型数据
    myDiagram.model = new go.GraphLinksModel(
    // 创建元素
    [
        { key: 'SomeNode1' },
        { key: 'SomeNode2' },
        { key: 'SomeNode3' },
    ],
    // 元素连线
    [
        { from: 'SomeNode1', to: 'SomeNode2' },
        { from: 'SomeNode1', to: 'SomeNode3' },
    ]
    );
}

onMounted(() => {
    initDiagram()
});
</script>