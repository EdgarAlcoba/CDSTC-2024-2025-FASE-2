import { useEffect, useState } from "react";
import PlannerResult from "../../components/PlannerResult/PlannerResult"
import Lottie from "lottie-react";
import * as location from "../../components/Assets/plane.json";
import * as success from "../../components/Assets/success.json";
import Navbar from "../../components/Navbar/Navbar";
import { Canvas } from "@react-three/fiber";
import { Experience } from "../../components/PlannerResult/Experience";
import { Loader } from "@react-three/drei";
import { useLocation, useNavigate } from "react-router-dom";

const Profile = () => {
    const navigate = useNavigate()
    const token = sessionStorage.getItem("token");

    const [tripList, setTripList] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:4040/trips", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "authorization": `${token}`,
            },
        })
            .then((response) => response.json())
            .then((json) => {
                setTripList(json)
            });
    }, []);

    const handleClick = (item) => {
        navigate("/plannerResult", {
            state: {
              json: item,
              type: "profile"
            }
          });
    }

    


    return (
        <div className="h-screen bg-white pt-1">
            <Navbar />
            <div className="flex flex-col items-center justify-center">
                {tripList.map((item, index) => (
                    <div key={index} className="p-4 m-2 bg-gray-200 hover:bg-gray-400 hover:cursor-pointer rounded flex space-x-10 w-10/12 items-center justify-center pl-1 pr-1" onClick={() => handleClick(item)}>
                        <div className="space-x-1 flex">
                            <span className="font-semibold">Destino:</span>
                            <p>{item.destination}</p>
                        </div>
                        <div className="space-x-1 flex">
                            <span className="font-semibold">Duración:</span>
                            <p>{item.duration}</p>
                        </div>
                        <div className="space-x-1 flex">
                            <span className="font-semibold">Fecha de reserva:</span>
                            <p>{item.generated_on}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Profile;
