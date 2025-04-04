import React from "react";
import Navbar from "../../components/Navbar/Navbar";
import "./Info.css";
import Logo from "../../components/Assets/SincoLogo.svg";

const Info = () => {
  return (
    <div className="">
      <Navbar />

      <div className="info-body">
        <div style={{ minHeight: "1rem" }}></div>
        <label className="welcome-label">Proyecto GreenTrip</label>
        <label className="about-us-label">Sobre nosotros</label>

        <label className="info-text">
          GreenTrip surge de la necesidad de atraer a turistas a la ciudad de
          GreenLake Village. 
        </label>
        <label className="info-text">
          Este proyecto ofrece al usuario una plataforma intuitiva para
          descubrir la ciudad y sus regiones, aportando datos como rutas,
          actividades o la ocupacion de los hoteles.
        </label>
        <label className="info-text">
          La IA nativa permite a los turistas planificar su viaje de manera comoda 
          e intuitiva, asegurandose de que se tenga siempre en cuenta 
          las preferencias del usuario.
        </label>
        <label className="info-text">
          No solo buscamos ayudar a los turistas sino que los dueños de los negocios de 
          GreenLake se beneficiaran tambien de las estadisticas que proporciona la aplicacion, 
          pudiendo visualizar de manera clara la afluencia de turistas. 
        </label>
        <label className="info-text">
          Tambien se proporciona informacion sobre sostenibilidad que las distintas autoridades 
          competentes encontraran muy util a la hora de planificar eventos o actividades en la ciudad.
        </label>

        <label className="about-us-label">Desarrollado por </label>
        <label className="creators">
          <img className="sinco" src={Logo} alt="Sinco" />
          <br></br>
          <ul>
            <li>Edgar Alcoba Casado</li>
            <li>Pablo Corral Gutiérrez</li>
            <li>Marcos Sarmiento Álvarez</li>
            <li>Víctor Frutos Martínez Calvo</li>
            <li>Pablo Morais Álvarez</li>
          </ul>
        </label>
      </div>
    </div>
  );
};

export default Info;
