<script lang="ts">
  import SchemaComparison from '../components/SchemaComparison.svelte';
    </script>
  
  <main>
    <section class="hero">
      <h1>Schema Comparison Tool</h1>
      <p>Effortlessly compare and analyze database schemas</p>
      <a href="/compare" class="cta-button">Start Comparing</a>
    </section>
  
    <SchemaComparison />

    <section class="features">
      <div class="feature">
        <h2>Visual Diff</h2>
        <p>See schema changes at a glance with our intuitive visual comparison.</p>
      </div>
      <div class="feature">
        <h2>Version History</h2>
        <p>Track schema evolution over time with comprehensive version control.</p>
      </div>
      <div class="feature">
        <h2>SQL Generation</h2>
        <p>Automatically generate SQL migration scripts based on schema differences.</p>
      </div>
    </section>

  </main>
  
  <style>
    main {
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem;
    }
  
    .hero {
      text-align: center;
      padding: 4rem 0;
    }
  
    h1 {
      font-size: 3rem;
      margin-bottom: 1rem;
    }
  
    .cta-button {
      display: inline-block;
      background-color: #4CAF50;
      color: white;
      padding: 0.8rem 1.5rem;
      text-decoration: none;
      border-radius: 5px;
      font-weight: bold;
      margin-top: 1rem;
    }
  
    .features {
      display: flex;
      justify-content: space-between;
      margin-top: 4rem;
    }
  
    .feature {
      flex: 1;
      padding: 1rem;
      text-align: center;
    }
  
    h2 {
      font-size: 1.5rem;
      margin-bottom: 0.5rem;
    }
  </style>
  
