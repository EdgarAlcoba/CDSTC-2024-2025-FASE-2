/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./node_modules/react-tailwindcss-datepicker/dist/index.esm.{js,ts}",
  ],
  theme: {
    extend: {
      colors: {
        'lapis-lazuli': '#22577a',
        'verdigris': '#38a3a5',
        'emerald': '#57cc99',
        'light-green': '#80ed99',
        'tea-green': '#c7f9cc',
      }
    },
  },
  plugins: [],
}

