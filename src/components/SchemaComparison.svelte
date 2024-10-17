<script lang="ts">
  import { onMount } from 'svelte';

  let schemas: any[] = [];
  let comparisonResult: any = null;
  let schema1: string = '';
  let schema2: string = '';

  onMount(async () => {
    // Fetch available schemas from the API
    const response = await fetch('/api/schemas');
    schemas = await response.json();
  });

  async function compareSchemas(schema1: string, schema2: string) {
    const response = await fetch('/api/schemas/compare', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ schema1, schema2 })
    });
    comparisonResult = await response.json();
  }
</script>

<div class="schema-comparison">
    <h2>Schema Comparison</h2>
    <div class="schema-selector">
      <select bind:value={schema1}>
        {#each schemas as schema}
          <option value={schema.name}>{schema.name}</option>
        {/each}
      </select>
      <select bind:value={schema2}>
        {#each schemas as schema}
          <option value={schema.name}>{schema.name}</option>
        {/each}
      </select>
      <button on:click={() => compareSchemas(schema1, schema2)}>Compare</button>
    </div>

    {#if comparisonResult}
    <div class="comparison-result">
      <h3>Comparison Results</h3>
      <div class="result-section">
        <h4>Added</h4>
        <ul>
          {#each comparisonResult.added as item}
            <li>{item}</li>
          {/each}
        </ul>
      </div>
      <div class="result-section">
        <h4>Removed</h4>
        <ul>
          {#each comparisonResult.removed as item}
            <li>{item}</li>
          {/each}
        </ul>
      </div>
      <div class="result-section">
        <h4>Modified</h4>
        <ul>
          {#each comparisonResult.modified as item}
            <li>{item}</li>
          {/each}
        </ul>
      </div>
    </div>
  {/if}
  

  </div>
  
  <style>
    .schema-comparison {
      margin-top: 2rem;
    }
    .schema-selector {
      display: flex;
      gap: 1rem;
      margin-bottom: 1rem;
    }
  </style>
  