<script lang="ts">
import { onMount } from 'svelte';
import * as d3 from 'd3';
import dagre from 'dagre-d3';

export let schemaComparison: any;

let svg;

onMount(() => {
  renderGraph();
});

function renderGraph() {
  const g = new dagre.graphlib.Graph().setGraph({});

  // Add nodes for each table
  Object.keys(schemaComparison).forEach(tableName => {
    g.setNode(tableName, { label: tableName, shape: 'rect' });
    
    // Add nodes for columns
    schemaComparison[tableName].forEach(column => {
      const columnId = `${tableName}_${column.name}`;
      g.setNode(columnId, { 
        label: column.name, 
        shape: 'ellipse',
        style: getColumnStyle(column.status)
      });
      g.setEdge(tableName, columnId, {});
    });
  });

  const render = new dagre.render();
  const svgGroup = d3.select(svg).append('g');
  render(svgGroup, g);

  // Add zoom behavior
  const zoom = d3.zoom().on('zoom', (event) => {
    svgGroup.attr('transform', event.transform);
  });
  d3.select(svg).call(zoom);
}

function getColumnStyle(status) {
  switch(status) {
    case 'added': return 'fill: #8f8';
    case 'removed': return 'fill: #f88';
    case 'modified': return 'fill: #ff8';
    default: return 'fill: #fff';
  }
}
</script>

<svg bind:this={svg}></svg>

<style>
svg {
  width: 100%;
  height: 600px;
  border: 1px solid #ccc;
}
</style>