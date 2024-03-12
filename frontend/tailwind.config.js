/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}", "./public/index.html"],

  theme: {
    extend: {
      colors: {
        white: "#ECF0FF",
        black: "#0E1012",
        "primary-100": "#DDE3FF",
        "primary-200": "#C2CBFF",
        "primary-300": "#9CA7FF",
        "primary-400": "#7E8AFF",
        primary: "#6673FF",
        "primary-600": "#4F5EFF",
        "primary-700": "#3F4CFF",
        "primary-800": "#3725AE",
        "neutral-100": "#E7E7E7",
        "neutral-200": "#D1D1D1",
        "neutral-300": "#B0B0B0",
        "neutral-400": "#888888",
        "neutral-500": "#6E6E6E",
      },
    },
  },
  plugins: [],
};
