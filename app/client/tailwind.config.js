/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: false,
  content: [],
  theme: {
    extend: {},
    colors: {
      primary: "#101827",
      secondary: "#3c82f6",
      white: "#fff",
      grey: "#777",
      bgGreyColor: "#949AA6",
    },
    fontFamily: {
      primary: "Montserrat",
      secondary: "Bebas Neue",
    },
  },
  plugins: [],
};
