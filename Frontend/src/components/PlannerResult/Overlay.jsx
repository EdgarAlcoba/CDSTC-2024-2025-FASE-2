import { Scroll, useScroll } from "@react-three/drei";
import { useFrame } from "@react-three/fiber";
import { useState } from "react";

const Section = (props) => {
  return (
    <section
      className={`h-screen flex flex-col justify-center p-10 ${props.right ? "items-end" : "items-start"}`}
      style={{
        opacity: props.opacity
      }}
    >
      <div className="w-1/2 flex items-center justify-center">
        <div className={`w-full ${props.itinerary ? "overflow-y-auto rounded-lg h-2/5" : "max-w-md"}`}>
          <div className="bg-white rounded-lg p-4 ">{props.children}</div>
        </div>
      </div>
    </section>
  );
};

const Overlay = (props) => {
  const cityName = props.city ? props.city : "";

  const scroll = useScroll();

  const [opacityFirstSection, setOpacityFirstSection] = useState(1);
  const [opacitySecondSection, setOpacitySecondSection] = useState(1);
  const [opacityThirdSection, setOpacityThirdSection] = useState(1);

  useFrame(() => {
    setOpacityFirstSection(1 - scroll.range(0, 1 / 3));
    setOpacitySecondSection(scroll.curve(1 / 3, 1 / 3));
    setOpacityThirdSection(scroll.range(2 / 3, 1 / 3));
  });

  const totalActivities = props.data.itinerary.reduce(
    (sum, day) => sum + day.activities.length,
    0
  );

  const cityDescriptions = {
    "Aruba Central": {
      slogan: '"El paraíso tropical brillante"',
      description: "Una isla tropical con playas paradisíacas y aguas cristalinas, ideal para relajarse o practicar deportes acuáticos como snorkel, buceo y windsurf. Su vibrante centro urbano ofrece mercados artesanales, gastronomía caribeña como el keshi yena y una animada vida nocturna."
    },
    "Nimble Peak": {
      slogan: '"El refugio de los Aventureros"',
      description: "Un destino de montaña que combina aventura y sostenibilidad, con picos ideales para escaladores y valles floridos para el senderismo. El transporte eléctrico y los trenes de alta velocidad conectan sus barrios, ofreciendo vistas panorámicas en un entorno donde la naturaleza y la tecnología conviven en armonía."
    },
    "Composable Cloud": {
      slogan: '"La Ciudad del Futuro"',
      description: "Una ciudad futurista con edificios modulares, tecnología en la nube que mueve desde coches autónomos hasta hologramas, y espacios interactivos como museos de IA y parques de realidad aumentada. Ideal para los amantes de la innovación."
    },
    "Ezmeral Valley": {
      slogan: '"El corazón verde y fértil"',
      description: "Un valle agrícola donde tradición y tecnología conviven. Granjas inteligentes con IA, rutas en bici entre viñedos y catas de vino orgánico, todo culmina en un colorido festival de la cosecha."
    },
    "ProLiant Village": {
      slogan: '"El pueblo Tecnológico con Alma"',
      description: "Un lugar que combina tecnología y calidez: cafés inteligentes, tiendas automatizadas y espacios ideales para nómadas digitales, sin perder su esencia local con mercados y festivales comunitarios. Perfecto para trabajar o desconectar."
    },
    "Apollo Heights": {
      slogan: '"La ciudad de las Estrellas"',
      description: "Un destino urbano y espacial con rascacielos, un puerto aeroespacial y experiencias como simuladores de gravedad cero, observatorios y lanzamientos de cohetes. Por la noche, los espectáculos de drones iluminan el cielo, haciendo de este un destino inolvidable para amantes del espacio."
    },
    "Simplivity Springs": {
      slogan: '"El Santuario del Bienestar"',
      description: "Rodeada de fuentes termales, es un refugio de paz. Con lujosos spas, retiros de yoga y jardines zen, ofrece el espacio perfecto para desconectar y encontrar serenidad en plena naturaleza."
    },
    "GreenLake Shores": {
      slogan: '"El Edén junto al Lago"',
      description: "Un entorno natural junto a un lago esmeralda, ideal para actividades como kayak, pesca y picnic. Destaca por su arquitectura ecológica y el uso de energías renovables, reflejando un fuerte compromiso con la sostenibilidad."
    },
    "Alletra City": {
      slogan: '"La Metrópoli Eléctrica"',
      description: "Una ciudad dinámica centrada en la movilidad sostenible, con trenes ultrarrápidos y bicis compartidas. El arte digital y los festivales de luces aportan un ambiente creativo y vibrante que nunca se apaga."
    },
    "HPE Innovation Hub": {
      slogan: '"El Epicentro del Progreso"',
      description: "Un centro de innovación con laboratorios de robótica, campus de startups y hackatones. Los visitantes pueden explorar exposiciones tecnológicas y asistir a charlas inspiradoras."
    },
  };

  const cityDescription = cityDescriptions[cityName] || "";

  return (
    <Scroll html>
      <div className="w-screen">
        <Section opacity={opacityFirstSection}>
          <h1 className="text-2xl font-bold">{cityName}</h1>
          <h2 className="text-md font-bold">{cityDescription.slogan}</h2>
          <p>{cityDescription.description}</p>
          <p className="font-semibold">Deslice hacia abajo para conocer su itinerario</p>
        </Section>
        <Section right opacity={opacitySecondSection}>
          <strong className="text-xl">Duración</strong>
          <p>{props.data.duration} {props.data.duration === 1 ? "día" : "días"} ☀️</p>
          <p>{props.data.duration} {props.data.duration === 1 ? "noche" : "noches"} 🌒 </p>
          <strong className="text-xl">Presupuesto</strong>
          <p>{props.data.budget}</p>
          <strong className="text-xl">Número de actividades</strong>
          <p>{totalActivities}</p>
        </Section>
        <Section opacity={opacityThirdSection} itinerary={true}>
          <strong className="text-2xl">Itinerario</strong>
          {props.data.itinerary.map((day, index) => (
            <div key={index} className="mt-4 p-4 border rounded-lg shadow-md">
              <h2 className="text-xl font-semibold">Día {day.day}</h2>
              <p className="font-bold">Hora | Actividad | Detalles | Ubicación</p>
              <ul className="list-disc pl-4">
                {day.activities.map((activity, i) => (
                  <li key={i} className="mt-2">
                    <span className="font-medium">{activity.time}</span>:{" "}
                    <span className="font-semibold">{activity.activity}</span><br />
                    <span>{activity.details}</span><br />
                    <span className="font-medium italic">{activity.location}</span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </Section>
      </div>
    </Scroll>
  );
};

export default Overlay;
