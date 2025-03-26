import { Loader } from "@react-three/drei";
import { Canvas } from "@react-three/fiber";
import { Suspense } from "react";
import { Experience } from "../../components/Magazine/Experience";
import { UI } from "../../components/Magazine/UI";
import Navbar from "../../components/Navbar/Navbar";
import "./Magazine.css";

const Magazine = () => {
  return (
    <div className="book-container">
      <Navbar />
      <Loader />
      <Canvas
        shadows
        camera={{
          position: [-0.5, 1, window.innerWidth > 800 ? 4 : 9],
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
  );
};

export default Magazine;
