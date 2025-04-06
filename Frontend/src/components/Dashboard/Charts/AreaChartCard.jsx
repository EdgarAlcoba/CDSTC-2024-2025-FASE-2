import React from "react";
import Chart from "react-apexcharts";

const AreaChartCard = ({title, description, variable, percentage, data, dates}) => {

  const chartOptions = {
    chart: {
      height: "100%",
      maxWidth: "100%",
      type: "area",
      fontFamily: "Inter, sans-serif",
      dropShadow: {
        enabled: false,
      },
      toolbar: {
        show: false,
      },
    },
    tooltip: {
      enabled: true,
      x: {
        show: false,
      },
    },
    fill: {
      type: "gradient",
      gradient: {
        opacityFrom: 0.55,
        opacityTo: 0,
        shade: "#50C878",
        gradientToColors: ["#50C878"],
      },
    },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      width: 8,
    },
    grid: {
      show: false,
      strokeDashArray: 4,
      padding: {
        left: 2,
        right: 2,
        top: 4
      },
    },
    series: [
      {
        name: variable,
        data: data,
        color: "#50C878",
      },
    ],
    xaxis: {
      categories: dates,
      labels: {
        show: false,
      },
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false,
      },
    },
    yaxis: {
      show: false,
    },
  }

  return (
    <div className="flex flex-col bg-white rounded shadow-sm  p-4 md:p-6 border border-stone-300 h-full">
      <div className="flex justify-between">
        <div>
          <p className="text-gray-700 font-bold mb-2 text-xl">{title}</p>
          <p className="text-stone-500 text-sm">{description}</p>
        </div>
      </div>

      {/* Gráfico de área */}
      <div id="area-chart" className="flex-grow">
        <Chart options={chartOptions} series={chartOptions.series} type="area" height={200} />
      </div>
    </div>
  );
};

export default AreaChartCard;
