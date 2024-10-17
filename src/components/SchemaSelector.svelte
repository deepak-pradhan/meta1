<script lang="ts">
  import { onMount } from 'svelte';

  let schemas = [];
  let selectedSchema1 = '';
  let selectedSchema2 = '';

  onMount(async () => {
    const response = await fetch('/api/schemas');
    schemas = await response.json();
  });

  function compareSchemas() {
    // We'll implement this function to trigger the comparison
  }
</script>

<div class="schema-selector">
  <h2>Select Schemas to Compare</h2>
  <div class="schema-dropdowns">
    <select bind:value={selectedSchema1}>
      <option value="">Select first schema</option>
      {#each schemas as schema}
        <option value={schema.name}>{schema.name}</option>
      {/each}
    </select>
    <select bind:value={selectedSchema2}>
      <option value="">Select second schema</option>
      {#each schemas as schema}
        <option value={schema.name}>{schema.name}</option>
      {/each}
    </select>
  </div>
  <button on:click={compareSchemas} disabled={!selectedSchema1 || !selectedSchema2}>
    Compare Schemas
  </button>
</div>

<style>
  .schema-selector {
    margin-top: 2rem;
  }
  .schema-dropdowns {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
  }
</style>