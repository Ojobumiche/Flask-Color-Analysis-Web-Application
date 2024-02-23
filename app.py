from flask import Flask, render_template
from collections import Counter
from statistics import variance
from colour import all_colors

app = Flask(__name__)


@app.route('/')
def bincon():
    return render_template('bincon.html')

# Extracting colors from the table
colors = [
    "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
]

# Combine all colors into a single list
all_colors = [color.strip() for day_colors in colors for color in day_colors.split(',')]

# Calculate the mean colour
mean_colour = Counter(all_colors).most_common(1)[0][0]

# Calculate the most common color
most_common_color = Counter(all_colors).most_common(1)[0][0]

# Calculate the median color
sorted_colors = sorted(all_colors)
n = len(sorted_colors)
median_color = sorted_colors[n // 2] if n % 2 != 0 else (sorted_colors[n // 2 - 1] + sorted_colors[n // 2]) / 2

# Calculate the variance of color frequencies
color_frequencies = Counter(all_colors).values()
colors_variance = variance(color_frequencies)

# Calculate the probability of choosing red
red_probability = Counter(all_colors)["RED"] / len(all_colors)


@app.route('/colour')
def colour():
    return render_template('colour.html',
                           mean_colour=mean_colour,
                           most_common_color=most_common_color,
                           median_color=median_color,
                           colors_variance=colors_variance,
                           red_probability=red_probability)

if __name__ == '__main__':
    app.run(debug=True)
