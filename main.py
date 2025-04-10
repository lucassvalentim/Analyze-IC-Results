import json
import os
import matplotlib.pyplot as plt

path = "OptimizationResults/dblp_resultsR1.json"

with open(path, 'r') as file:
    data = json.load(file)

iterations = data.get("iteration", {})

best_macro_f1 = -1
best_prompt = ""

# Dados para os gráficos
all_macros = [] 
all_iter_labels = []
iteration_means = []

iteration_id = 0
for instructions in iterations.values():
    macro_f1_values = []
    respective_prompts = []

    for instruction_name, values in instructions.items():
        macro_f1 = values["macro_f1"]
        prompt = values["response_prompt"]

        macro_f1_values.append(macro_f1)
        respective_prompts.append(prompt)

        all_macros.append(macro_f1)
        all_iter_labels.append(int(iteration_id))  # CORREÇÃO AQUI
    iteration_id += 1
    iteration_means.append(sum(macro_f1_values)/len(macro_f1_values))

# Criar pasta se quiser salvar em pasta
# os.makedirs("figures", exist_ok=True)

# Gráfico 1 - Todos os pontos por iteração
plt.figure(figsize=(10, 6))
scatter = plt.scatter(all_iter_labels, all_macros, c=all_iter_labels, cmap="viridis", alpha=0.7)
plt.colorbar(scatter, label="Iteração")
plt.xlabel("Iteração")
plt.ylabel("Macro F1")
plt.title("Distribuição dos macro-F1 por iteração")
plt.grid(True)
plt.savefig("./macros_por_iteracao_pontos_dblp.png")

# Gráfico 2 - Média por iteração
sorted_iteration_ids = sorted([i for i in iterations.keys()])
plt.figure(figsize=(10, 6))
plt.plot(sorted_iteration_ids, iteration_means, marker="o", color="blue")
plt.xlabel("Iteração")
plt.ylabel("Média Macro F1")
plt.title("Média do Macro F1 por Iteração")
plt.grid(True)
plt.savefig("./media_macros_por_iteracao_dblp.png")