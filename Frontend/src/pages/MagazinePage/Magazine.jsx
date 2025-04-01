import { Loader } from "@react-three/drei";
import { Canvas } from "@react-three/fiber";
import { Suspense } from "react";
import { Experience } from "../../components/Magazine/Experience";
import { UI } from "../../components/Magazine/UI";
import Navbar from "../../components/Navbar/Navbar";
import "./Magazine.css";
import { useAtom } from "jotai";
import { pageAtom } from "../../components/Magazine/UI";
import { Link } from "react-router-dom";

const Magazine = () => {
  const cityNames = {
    0: "GreenLake Village",
    1: "Aruba Central",
    2: "Nimble Peak",
    3: "Compostable Cloud",
    4: "Ezmeral Valley",
    5: "Proliant Village",
    6: "Apollo Heights",
    7: "Simplicity Springs",
    8: "Greenlake Shores",
    9: "Alletra City",
    10: "HPE Innovation Hub",
    11: "GreenLake Village",
  };

  const [page] = useAtom(pageAtom);

  const cityName = cityNames[page] || "Unknown";

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
            Hotel-rating Lorem Ipsum is simply dummy text of the printing and
            typesetting industry. Lorem Ipsum has been the industry's standard
            dummy text ever since the 1500s, when an unknown printer took a
            galley of type and scrambled it to make a type specimen book. It has
            survived not only five centuries, but also the leap into electronic
            typesetting, remaining essentially unchanged. It was popularised in
            the 1960s with the release of Letraset sheets containing Lorem Ipsum
            passages, and more recently with desktop publishing software like
            Aldus PageMaker including versions of Lorem Ipsum.
          </p>
          <Link to="/travelplanner">
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
