# AI Atlas Nexus - Summarization

## Executive Summary

AI Atlas Nexus is an open-source governance toolkit for foundation-model systems. It brings together AI risk taxonomies, mitigation actions, evaluation resources, and AI system metadata in a single ontology-backed knowledge graph so teams can turn high-level governance requirements into practical implementation steps.

## What this can be used for

- Identify and prioritize risks for a specific AI use case.
- Map risks to governance controls, principles, and mitigation actions.
- Find related evaluations and benchmarks for safety and quality validation.
- Export ontology data into graph databases for enterprise governance workflows.
- Accelerate governance documentation and questionnaire workflows.

## How to add your own taxonomy

1. Add one or more YAML files to `src/ai_atlas_nexus/data/knowledge_graph/`.
2. Ensure your entries follow the ontology schema documented at `docs/ontology/index.md`.
3. Define risks/actions/taxonomies in YAML. Example:

```yaml
- id: my-own-risk
  name: A very risky AI behaviour
  description: An LLM-based system is often very risky
  isDefinedByTaxonomy: my-taxonomy
```

4. (Optional) Add cross-taxonomy mappings in TSV format and run `make lift_mappings_from_tsv` to generate LinkML YAML mappings.
5. Follow the full contribution guide for taxonomy files, mappings, and CoT templates: [Contributing a taxonomy](docs/concepts/Contributing_a_taxonomy.md).

## Example screenshots

### Architecture view

![Architecture](https://github.com/IBM/ai-atlas-nexus/blob/main/resources/images/architecture.png?raw=true)

### Risk taxonomy view

![IBM AI Risk Atlas categories](https://github.com/IBM/ai-atlas-nexus/blob/main/docs/assets/ibm_ai_risk_atlas.png?raw=true)

## Costs

AI Atlas Nexus is licensed under Apache 2.0 and is free to use.

Operational cost depends on your deployment setup:

- **Inference/API costs:** charges from hosted model providers.
- **Infrastructure costs:** compute, storage, and database hosting for self-managed deployments.
- **Implementation costs:** engineering effort to integrate with existing governance systems.

Using local model inference can reduce API spend but may increase infrastructure and operations overhead.
