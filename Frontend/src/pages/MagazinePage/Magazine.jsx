import { Loader } from "@react-three/drei";
import { Canvas } from "@react-three/fiber";
import { Suspense } from "react";
import { Experience } from "../../components/Magazine/Experience";
import { UI } from "../../components/Magazine/UI";
import Navbar from "../../components/Navbar/Navbar";
import { useAtom } from "jotai";
import { pageAtom } from "../../components/Magazine/UI";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";

const Magazine = () => {
  const token = sessionStorage.getItem("token");

  const cityNames = {
    0: "GreenLake Village",
    1: "Aruba Central",
    2: "Nimble Peak",
    3: "Composable Cloud",
    4: "Ezmeral Valley",
    5: "ProLiant Village",
    6: "Apollo Heights",
    7: "Simplivity Springs",
    8: "GreenLake Shores",
    9: "Alletra City",
    10: "HPE Innovation Hub",
    11: "GreenLake Village",
  };

  const [page] = useAtom(pageAtom);

  const cityName = cityNames[page] || "Unknown";

  const [hotelsData, setHotelsData] = useState([]);

  useEffect(() => {
    const fetchHotels = async () => {
      fetch("http://127.0.0.1:4040/cities/hotelRatings")
        .then((response) => {
          if (!response.ok) throw new Error("Error al obtener los datos");
          return response.json();
        })
        .then((data) => {
          setHotelsData(data);
        })
        .catch((err) => {
          console.log("Error fetching hotels:", err.message);
        });
    };

    fetchHotels();
  }, []);

  const cityData = hotelsData.find((city) => city.name === cityName);
  const hotels = cityData ? cityData.hotels : [];

  return (
    <div className="page-container min-h-screen w-full">
      <Navbar />
      <section className="flex h-full w-full flex-col lg:flex-row lg:items-center">
        <div className="book-container h-[70dvh] w-full lg:min-h-screen lg:w-[69dvw]">
          <Loader />
          <Canvas
            shadows
            camera={{
              position: [-0.5, 1, window.innerWidth > 1500 ? 4 : 5],
              fov: 45,
            }}
          >
            <group position-y={0}>
              <Suspense fallback={null}>
                <Experience />
              </Suspense>
            </group>
          </Canvas>
          <UI />
        </div>
        <div className="flex flex-col items-center bg-white/40 rounded-xl shadow-xl p-4 h-auto w-full lg:min-h-full lg:w-[28dvw]">
          <h1 className="text-4xl font-medium mb-2">{cityName}</h1>
          <p>
            {hotels.length > 0 ? (
              <>
                <strong>Hotel Ratings:</strong>
                <ul className="mt-2">
                  {hotels.map((hotel, index) => (
                    <li key={index}>
                      {hotel.hotel_name} - ⭐ {hotel.average_rating}
                    </li>
                  ))}
                </ul>
              </>
            ) : (
              <></>
            )}
          </p>
          <Link to={token ? "/travelplanner": "/login"}>
            <button
              className={`bg-white hover:bg-blue-400 hover:shadow-xl transition-all duration-300 px-4 py-3 rounded-full text-lg uppercase border border-transparent mt-2`}
            >
              Planifica tu viaje
            </button>
          </Link>
        </div>
      </section>
    </div>
  );
};

export default Magazine;
