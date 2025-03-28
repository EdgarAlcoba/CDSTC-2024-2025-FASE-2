import React, {useEffect} from "react";
import Chart from "react-apexcharts";
import { useDate } from "../../../hooks/DateContext";

const AreaChartCard = ({title, variable, percentage, data, dates}) => {

  const { date } = useDate();

  useEffect(() => {
      console.log('Han cambiado fecha, llamar a la API');
      /* Llamadas a back y demás */
  }, [date]);

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
      width: 6,
    },
    grid: {
      show: false,
      strokeDashArray: 4,
      padding: {
        left: 2,
        right: 2,
        top: 0
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
    <div className="bg-white rounded shadow-sm  p-4 md:p-6 border border-stone-300">
      <div className="flex justify-between">
        <div>
          <h5 className="text-3xl font-bold text-gray-900  pb-2">32.4k</h5>
          <p className="text-base font-normal text-gray-500 ">{title}</p>
        </div>
        <div className="flex items-center px-2.5 py-0.5 text-base font-semibold text-green-500">
          {percentage}
          <svg
            className="w-3 h-3 ms-1"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 10 14"
          >
            <path
              stroke="currentColor"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M5 13V1m0 0L1 5m4-4 4 4"
            />
          </svg>
        </div>
      </div>

      {/* Gráfico de área */}
      <div id="area-chart">
        <Chart options={chartOptions} series={chartOptions.series} type="area" height={200} />
      </div>
    </div>
  );
};

export default AreaChartCard;
