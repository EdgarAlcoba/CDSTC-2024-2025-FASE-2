import { OrbitControls, ScrollControls } from "@react-three/drei";
import Overlay from "./Overlay";

import { ArubaCentral } from "./ModelComponents/ArubaCentral";
import { NimblePeak } from "./ModelComponents/NimblePeak";
import { ComposableCloudl } from "./ModelComponents/ComposableCloud";
import { EzmeralValley } from "./ModelComponents/EzmeralValley";
import { ProLiantVillage } from "./ModelComponents/ProLiantVillage";
import { ApolloHeights } from "./ModelComponents/ApolloHeights";
import { SimplivitySprings } from "./ModelComponents/SimplivitySprings";
import { GreenLakeShores } from "./ModelComponents/GreenLakeShores";
import { AlletraCity } from "./ModelComponents/AlletraCity";
import { HPEInnovationHub } from "./ModelComponents/HPEInnovationHub";

export const Experience = (props) => {
  const cityComponents = {
    "Aruba Central": ArubaCentral,
    "Nimble Peak": NimblePeak,
    "Composable Cloud": ComposableCloudl,
    "Ezmeral Valley": EzmeralValley,
    "ProLiant Village": ProLiantVillage,
    "Apollo Heights": ApolloHeights,
    "Simplivity Springs": SimplivitySprings,
    "GreenLake Shores": GreenLakeShores,
    "Alletra City": AlletraCity,
    "HPE Innovation Hub": HPEInnovationHub,
  };

  const CityComponent = cityComponents[props.city] || null;
  return (
    <>
      <ambientLight intensity={2} />
      <ScrollControls pages={3} damping={0.25}>
        <Overlay city={props.city} data={props.data}/>
        {CityComponent && <CityComponent />}
      </ScrollControls>
    </>
  );
};
