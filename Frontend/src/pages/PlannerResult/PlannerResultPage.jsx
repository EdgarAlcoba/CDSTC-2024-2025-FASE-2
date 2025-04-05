import { useEffect, useState } from "react";
import PlannerResult from "../../components/PlannerResult/PlannerResult"
import Lottie from "lottie-react";
import * as location from "../../components/Assets/plane.json";
import * as success from "../../components/Assets/success.json";
import Navbar from "../../components/Navbar/Navbar";
import { Canvas } from "@react-three/fiber";
import { Experience } from "../../components/PlannerResult/Experience";
import { Loader } from "@react-three/drei";
import { useLocation } from "react-router-dom";

const PlannerResultPage = () => {
    const token = sessionStorage.getItem("token");

    const [data, setData] = useState({})
    const [loading, setLoading] = useState(false);
    const [completed, setCompleted] = useState(false);


    const loc = useLocation();

    useEffect(() => {
        const { json, type } = loc.state || {};
        console.log("Tipo:", type, " - Tipo real:", typeof type);
        if (type === "trip") {
            setTimeout(() => {
                fetch("http://127.0.0.1:4040/planTrip", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "authorization": `${token}`,
                    },
                    body: JSON.stringify(json),
                })
                    .then((response) => response.json())
                    .then((json) => {
                        setLoading(true);
                        setData(json);

                        setTimeout(() => {
                            setCompleted(true);
                        }, 1000);
                    });
            }, 3000);
        } else {
            setLoading(true);
            setCompleted(true);
            setData(json);
        }
    }, []);


    const cameraSpecs = {
        "Aruba Central": {
            fov: 104,
            position: [2.8, 1.5, 3.3],
        },
        "Nimble Peak": {
            fov: 84,
            position: [0.40, 0.3, 0.4],
        },
        "Composable Cloud": {
            fov: 54,
            position: [0.3, 1.0, 1.8],
        },
        "Ezmeral Valley": {
            fov: 84,
            position: [2.3, 2.0, 2.3],
        },
        "ProLiant Village": {
            fov: 94,
            position: [2.3, 2.0, 2.3],
        },
        "Apollo Heights": {
            fov: 84,
            position: [2.3, 2.0, 2.3],
        },
        "Simplivity Springs": {
            fov: 84,
            position: [2.3, 2.0, 2.3],
        },
        "GreenLake Shores": {
            fov: 74,
            position: [1.0, 0.4, 1.0],
        },
        "Alletra City": {
            fov: 74,
            position: [100.0, 40.0, 100.0],
        },
        "HPE Innovation Hub": {
            fov: 34,
            position: [1.2, 0.8, 0.9],
        },
    };

    const camera = cameraSpecs[data.destination] || [];

    return (
        !completed ? (
            <div className="bg-slate-100 pt-1">
                <Navbar />
                <div className=" flex flex-col items-center justify-center h-screen">
                    {!loading ? (
                        <>
                            <div className="bg-gray-200 rounded-xl p-4 flex flex-col items-center justify-center">
                                <p className="font-2xl font-bold mb-2  items-center justify-center">Nuestra IA está buscando su destino ideal</p>
                                <p className="font-x  items-center justify-centerl">Espere unos instantes para descubrirlo</p>
                            </div>
                            <Lottie animationData={location.default} style={{ height: "60vh", width: "60vh" }} />
                        </>
                    ) : (
                        <Lottie animationData={success.default} style={{ height: "20vh", width: "20vh" }} />
                    )}
                </div>
            </div>
        ) : (
            <div style={{ height: "100dvh", width: "100dvw" }}>
                <Navbar />
                <Loader />
                <Canvas
                    camera={{
                        fov: camera.fov,
                        position: camera.position,
                    }}
                >
                    <Experience city={data.destination} data={data} />
                </Canvas>
            </div>
        )
    );
};

export default PlannerResultPage;
