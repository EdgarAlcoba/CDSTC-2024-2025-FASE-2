import React, { useRef, useEffect } from 'react'
import { Link } from 'react-router-dom';
import Navbar from '../../components/Navbar/Navbar'
import './Home.css'
import videoBG from '../../components/Assets/HomeBackground.mp4'

const Home = () => {
  const videoRef = useRef(null);

  useEffect(() => {
    if (videoRef.current) {
      videoRef.current.playbackRate = 0.9;
    }
  }, []);

  return (
    <div className='min-h-screen w-screen flex flex-col object-contain bg-tea-green bg-opacity-20'>
      <Navbar />
      <video ref={videoRef} src={videoBG} autoPlay loop muted />

      <div className='flex flex-col items-center justify-center h-[80vh] space-y-5'>
        <label className='text-black text-7xl font-bold'>GreenTrip</label>
        <label className='text-black text-3xl'>Your smart travel planner</label>
        <Link to='/register'>
          <button className='px-7 py-3.5 bg-emerald text-black outline-none border-none rounded-[5rem] text-[1.5rem] 
          font-thin cursor-pointer transition duration-200 hover:shadow-2xl hover:bg-tea-green shadow-md'>Get started</button>
        </Link>
      </div>

    </div>
  )
}

export default Home