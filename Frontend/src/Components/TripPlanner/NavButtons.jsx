import React from 'react';
import { Link } from 'react-router-dom';

const NavButtons = ({ onBack, onNext, disabledNext, disabledBack, submitReady }) => {
  return (
    <div className="flex justify-between items-center mt-8">
      
      <button
        onClick={onBack}
        disabled={disabledBack}
        className="px-6 py-2 bg-gray-300 text-gray-700 rounded-lg hover:bg-gray-400 focus:outline-none"
      >
        Atrás
      </button>

      <button
        onClick={onNext}
        disabled={disabledNext}
        className={"px-6 py-2 bg-gray-300 text-gray-700 rounded-lg hover:bg-gray-400 focus:outline-none"}
      >
        {submitReady ? "Planificar viaje" : "Siguiente"}
      </button>

      <Link to="/">
        <button
        className={"px-6 py-2 bg-gray-300 text-gray-700 rounded-lg hover:bg-gray-400 focus:outline-none"}>
          Salir
        </button>
      </Link>
    </div>
  );
};

export default NavButtons;
