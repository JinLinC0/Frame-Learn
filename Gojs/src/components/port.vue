<template>
    <div id="diagramDiv" style="width: 100%; height: 900px; background-color: #DAE4E4;"></div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import go from 'gojs';

const $ = go.GraphObject.make;

var myDiagram: any;

function initDiagram() {

    myDiagram = $(go.Diagram, "diagramDiv", {
        'undoManager.isEnabled': true, // 启用撤销重做功能
        contentAlignment: go.Spot.Center, // 元素位置移动后始终处于在画布正中间
    });

    myDiagram.nodeTemplate =
        $(go.Node, "Auto",
        $(go.Shape, "Rectangle", { fill: "lightgray" }),
        $(go.Panel, "Table",
            $(go.RowColumnDefinition,
            { column: 0, alignment: go.Spot.Left}),
            $(go.RowColumnDefinition,
            { column: 2, alignment: go.Spot.Right }),
            $(go.TextBlock,  // the node title
            { column: 0, row: 0, columnSpan: 3, alignment: go.Spot.Center,
                font: "bold 10pt sans-serif", margin: new go.Margin(4, 2) },
            new go.Binding("text", "key")),

            $(go.Panel, "Horizontal",
                { column: 0, row: 1 },
                $(go.Shape,  // A端口
                    { 
                        width: 6,
                        height: 6, 
                        portId: "A", 
                        toSpot: go.Spot.Left,
                        toLinkable: true,   // 设置可连接
                        toMaxLinks: 1   // 最多只能连接一个
                    }
                ),
                $(go.TextBlock, "A")
            ),
            $(go.Panel, "Horizontal",
                { column: 0, row: 2 },
                $(go.Shape,  // B端口
                    { 
                        width: 6, 
                        height: 6, 
                        portId: "B", 
                        toSpot: go.Spot.Left,
                        toLinkable: true,   // 设置可连接
                        toMaxLinks: 1   // 最多只能连接一个
                    }
                ),
                $(go.TextBlock, "B")
            ),

            $(go.Panel, "Horizontal",
                { column: 2, row: 1, rowSpan: 2 },
                $(go.TextBlock, "Out"),  // out端口名称在布局的左边
                $(go.Shape,  // Out端口样式在布局的右边
                    { 
                        width: 6, 
                        height: 6, 
                        portId: "Out", 
                        fromSpot: go.Spot.Right,
                        fromLinkable: true
                    }
                )
            )
        )
        );

    myDiagram.linkTemplate =
        $(go.Link,
        { routing: go.Routing.Orthogonal, corner: 3 },
        $(go.Shape),
        $(go.Shape, { toArrow: "Standard" })
        );

    myDiagram.layout = $(go.LayeredDigraphLayout, { columnSpacing: 10 });

    var nodeDataArray = [
            { key: "Add1" },
            { key: "Add2" },
            { key: "Subtract1" }
    ];

    var linkDataArray = [
            { from: "Add1", fromPort: "Out", to: "Subtract1", toPort: "A" },
            { from: "Add2", fromPort: "Out", to: "Subtract1", toPort: "B" }
    ];

    myDiagram.model =
        $(go.GraphLinksModel,
        { 
            linkFromPortIdProperty: "fromPort",  
            linkToPortIdProperty: "toPort",
            nodeDataArray: nodeDataArray,
            linkDataArray: linkDataArray
        }
    );
}


onMounted(() => {
    initDiagram()
});
</script>