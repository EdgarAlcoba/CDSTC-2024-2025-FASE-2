import React from "react";

const Map = () => {
  return (
    <div className="flex flex-col col-span-6 p-4 rounded border border-stone-300">
      <div className="p-4">
        <h3 className="text-base font-normal text-gray-500">
          GreenLake Village Map
        </h3>
      </div>
      <svg
        viewBox="0 0 800 700"
        xmlns="http://www.w3.org/2000/svg"
        preserveAspectRatio="xMidYMid meet"
        className="w-full h-auto"
      >
        <rect width="800" height="700" fill="#e0f7fa" />

        <polygon
          points="350,250 450,220 470,300 380,320"
          fill="#a5d6a7"
          stroke="#388e3c"
          stroke-width="2"
        />
        <text x="390" y="270" font-size="14" fill="black">
          Aruba Central
        </text>

        <polygon
          points="300,100 480,80 510,160 330,170"
          fill="#81c784"
          stroke="#2e7d32"
          stroke-width="2"
        />
        <text x="370" y="130" font-size="14" fill="black">
          Nimble Peak
        </text>

        <polygon
          points="500,200 580,220 560,320 470,300"
          fill="#64b5f6"
          stroke="#1e88e5"
          stroke-width="2"
        />
        <text x="510" y="270" font-size="14" fill="black">
          Composable Cloud
        </text>

        <polygon
          points="220,220 300,200 330,320 250,350"
          fill="#ffb74d"
          stroke="#f57c00"
          stroke-width="2"
        />
        <text x="260" y="280" font-size="14" fill="black">
          Ezmeral Valley
        </text>

        <polygon
          points="470,330 580,350 540,440 440,420"
          fill="#ba68c8"
          stroke="#7b1fa2"
          stroke-width="2"
        />
        <text x="490" y="380" font-size="14" fill="black">
          ProLiant Village
        </text>

        <polygon
          points="300,350 390,340 420,420 320,440"
          fill="#f06292"
          stroke="#c2185b"
          stroke-width="2"
        />
        <text x="350" y="380" font-size="14" fill="black">
          Apollo Heights
        </text>

        <polygon
          points="200,150 270,100 300,200 220,220"
          fill="#26c6da"
          stroke="#00838f"
          stroke-width="2"
        />
        <text x="230" y="170" font-size="14" fill="black">
          Simplicity Springs
        </text>

        <polygon
          points="520,80 630,100 610,200 500,200"
          fill="#ffcc80"
          stroke="#ff9800"
          stroke-width="2"
        />
        <text x="540" y="150" font-size="14" fill="black">
          GreenLake Shores
        </text>

        <polygon
          points="350,450 430,460 420,650 340,640"
          fill="#90caf9"
          stroke="#1565c0"
          stroke-width="2"
        />
        <text x="360" y="500" font-size="14" fill="black">
          Alletra City
        </text>

        <polygon
          points="150,400 260,380 300,460 190,480"
          fill="#ff8a65"
          stroke="#d84315"
          stroke-width="2"
        />
        <text x="200" y="430" font-size="14" fill="black">
          HPE Innovation Hub
        </text>
      </svg>
    </div>
  );
};

export default Map;
