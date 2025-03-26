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
    <div className='home-container'>
      <Navbar />
      <video ref={videoRef} src={videoBG} autoPlay loop muted />
      <div className='home-body'>
        <label className='welcome-label'>Welcome to Eco...</label>
        <label className='fist-aid-label'>Your smart travel planner</label>
        <Link to='/register'>
          <button className='home-start-button'>Get started</button>
        </Link>
      </div>
    </div>
  )
}

export default Home