from bert_score import score

# Generated summary from the model
generated_summaries = [
    "Electric vehicles (EVs) are emerging as a key solution to reduce greenhouse gas emissions, reliance on fossil fuels, and urban pollution. In countries like Norway, EV adoption has skyrocketed, with over 54% of new car sales being electric vehicles in recent years.Governments around the globe are offering incentives for consumers to switch to electric vehicles. automotive manufacturers are investing heavily in research and development to create more efficient, affordable, and long-range electric cars."
]

# Reference summaries for comparison
reference_summaries = [
    "The transportation sector is transforming to combat climate change, with electric vehicles (EVs) merging as a key solution to reduce greenhouse gas emissions and urban pollution. Governments everwhere are incentivizing consumers to adopt EVs, while automakers are investing in research to develop more efficient, affordable, and long-range electric cars. Particularly in Norway, where over 54% of new car sales are electric."
]

# Compute BERTScore
P, R, F1 = score(generated_summaries, reference_summaries, lang="en", model_type="bert-base-uncased")

# Print F1 score (most commonly used metric)
print(f"Precision: {P.mean().item():.4f}")
print(f"Recall: {R.mean().item():.4f}")
print(f"F1 Score: {F1.mean().item():.4f}")
