import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": [
        "Laptop", "Mobile", "Headphones", "Keyboard", "Mouse",
        "Monitor", "Tablet", "Printer", "Smartwatch", "Camera",
        "Laptop", "Mobile", "Headphones", "Keyboard", "Mouse",
        "Monitor", "Tablet", "Printer", "Smartwatch", "Camera"
    ],

    "Category": [
        "Electronics", "Electronics", "Accessories", "Accessories", "Accessories",
        "Electronics", "Electronics", "Electronics", "Electronics", "Electronics",
        "Electronics", "Electronics", "Accessories", "Accessories", "Accessories",
        "Electronics", "Electronics", "Electronics", "Electronics", "Electronics"
    ],

    "Sales": [
        75000, 45000, 12000, 8000, 6000,
        35000, 40000, 28000, 18000, 55000,
        68000, 52000, 15000, 9000, 7000,
        30000, 42000, 25000, 20000, 60000
    ],

    "Cost": [
        60000, 38000, 8500, 5500, 4000,
        27000, 33000, 22000, 14000, 44000,
        55000, 43000, 10500, 6000, 4500,
        24000, 34000, 20000, 15500, 48000
    ],

    "Discount": [
        5, 10, 15, 20, 25,
        10, 15, 20, 25, 5,
        10, 15, 20, 25, 30,
        5, 10, 15, 20, 10
    ]
}

df = pd.DataFrame(data)

# Calculate Profit
df["Profit"] = df["Sales"] - df["Cost"]

# Create Discount Range
df["Discount Range"] = pd.cut(
    df["Discount"],
    bins=[0, 10, 20, 30],
    labels=["Low (1-10%)", "Medium (11-20%)", "High (21-30%)"]
)



total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
average_discount = df["Discount"].mean()
total_transactions = len(df)


sales_discount = df.groupby(
    "Discount Range",
    observed=True
)["Sales"].sum()

category_profit = df.groupby(
    "Category",
    observed=True
)["Profit"].sum()

category_discount = df.groupby(
    "Category",
    observed=True
)["Discount"].mean()

best_discount = sales_discount.idxmax()
best_category = category_profit.idxmax()



print("\n==========================================")
print("       DISCOUNT IMPACT ANALYSIS")
print("==========================================")

print("Total Sales       :", total_sales)
print("Total Profit      :", total_profit)
print("Average Discount  :", round(average_discount, 2), "%")
print("Total Transactions:", total_transactions)

print("\n==========================================")
print("          KEY RECOMMENDATIONS")
print("==========================================")

print("1. Focus on low discount ranges because they generate the highest sales.")
print("2. Give more attention to Electronics because it is the most profitable category.")
print("3. Avoid unnecessary high discounts because they can reduce profit.")



fig = plt.figure(figsize=(15, 9))

fig.patch.set_facecolor("#ffffff")

fig.suptitle(
    "DISCOUNT IMPACT ANALYSIS DASHBOARD",
    fontsize=20,
    fontweight="bold",
    y=0.97
)



box1 = fig.add_axes([0.05, 0.82, 0.20, 0.08])
box2 = fig.add_axes([0.28, 0.82, 0.20, 0.08])
box3 = fig.add_axes([0.51, 0.82, 0.20, 0.08])
box4 = fig.add_axes([0.74, 0.82, 0.20, 0.08])

boxes = [
    (box1, "TOTAL SALES", f"₹{total_sales:,}"),
    (box2, "TOTAL PROFIT", f"₹{total_profit:,}"),
    (box3, "AVERAGE DISCOUNT", f"{average_discount:.1f}%"),
    (box4, "TRANSACTIONS", str(total_transactions))
]

for box, title, value in boxes:

    box.set_facecolor("#f1f8f8")
    box.set_xticks([])
    box.set_yticks([])

    for side in box.spines.values():
        side.set_color("#4b9c9c")
        side.set_linewidth(1.5)

    box.text(
        0.5,
        0.65,
        title,
        ha="center",
        fontsize=10,
        fontweight="bold"
    )

    box.text(
        0.5,
        0.28,
        value,
        ha="center",
        fontsize=16,
        fontweight="bold",
        color="#287f82"
    )



ax1 = fig.add_axes([0.07, 0.52, 0.40, 0.24])

ax1.bar(
    sales_discount.index.astype(str),
    sales_discount.values,
    width=0.50,
    color="#5b9ea0"
)

ax1.set_title(
    "Sales by Discount Range",
    fontsize=12,
    fontweight="bold",
    pad=8
)

ax1.set_xlabel(
    "Discount Range",
    labelpad=5
)

ax1.set_ylabel(
    "Total Sales",
    labelpad=5
)

ax1.tick_params(axis="x", rotation=5)

ax1.grid(
    axis="y",
    linestyle="--",
    alpha=0.25
)

ax1.set_axisbelow(True)


ax2 = fig.add_axes([0.55, 0.52, 0.40, 0.24])

ax2.scatter(
    df["Discount"],
    df["Profit"],
    s=55,
    color="#5b9ea0",
    alpha=0.75
)

ax2.set_title(
    "Discount vs Profit",
    fontsize=12,
    fontweight="bold",
    pad=8
)

ax2.set_xlabel(
    "Discount (%)",
    labelpad=5
)

ax2.set_ylabel(
    "Profit",
    labelpad=5
)

ax2.grid(
    linestyle="--",
    alpha=0.25
)

ax2.set_axisbelow(True)



ax3 = fig.add_axes([0.07, 0.16, 0.40, 0.24])

ax3.bar(
    category_profit.index,
    category_profit.values,
    width=0.45,
    color="#7aa6a8"
)

ax3.set_title(
    "Category Wise Profit",
    fontsize=12,
    fontweight="bold",
    pad=8
)

ax3.set_xlabel(
    "Category",
    labelpad=5
)

ax3.set_ylabel(
    "Total Profit",
    labelpad=5
)

ax3.grid(
    axis="y",
    linestyle="--",
    alpha=0.25
)

ax3.set_axisbelow(True)


ax4 = fig.add_axes([0.55, 0.16, 0.40, 0.24])

ax4.bar(
    category_discount.index,
    category_discount.values,
    width=0.45,
    color="#8bb7b8"
)

ax4.set_title(
    "Average Discount by Category",
    fontsize=12,
    fontweight="bold",
    pad=8
)

ax4.set_xlabel(
    "Category",
    labelpad=5
)

ax4.set_ylabel(
    "Average Discount (%)",
    labelpad=5
)

ax4.grid(
    axis="y",
    linestyle="--",
    alpha=0.25
)

ax4.set_axisbelow(True)



recommendation_box = fig.add_axes(
    [0.07, 0.055, 0.88, 0.045]
)

recommendation_box.set_facecolor("#f7f7f7")
recommendation_box.set_xticks([])
recommendation_box.set_yticks([])

for side in recommendation_box.spines.values():
    side.set_color("#999999")
    side.set_linewidth(1)

recommendation_text = (
    "RECOMMENDATIONS  |  Focus on low discounts  |  "
    "Promote Electronics  |  Control unnecessary high discounts"
)

recommendation_box.text(
    0.5,
    0.5,
    recommendation_text,
    ha="center",
    va="center",
    fontsize=8.5,
    fontweight="bold"
)



plt.savefig(
    "discount_impact_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nDashboard image saved as:")
print("discount_impact_dashboard.png")



plt.show()