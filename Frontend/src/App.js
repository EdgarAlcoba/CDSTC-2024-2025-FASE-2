import './App.css';
//import FacebookLogin from '@greatsumini/react-facebook-login';
import LoginForm from './pages/LoginForm/LoginForm';
import RegisterForm from './pages/RegisterForm/RegisterForm';
import Home from './pages/HomePage/Home';
import Info from './pages/InfoPage/Info';
import Chat from './pages/Chat/Chat';
import Magazine from './pages/MagazinePage/Magazine'
import TripPlanner from './pages/TripPlanner/TripPlanner';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard/Dashboard';
import Map from './components/Map/Map'
import PlannerResultPage from './pages/PlannerResult/PlannerResultPage';
import Profile from './pages/Profile/Profile'

function App() {
  //let inicio = false;

  function getComp() {
    /*if(inicio){
      return(<LoginForm></LoginForm>);
    } else {
      return(<RegisterForm></RegisterForm>);
    }*/
  }
  return (
    <div className="min-h-screen">
      <Router>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/info' element={<Info />} />
          <Route path='/login' element={<LoginForm />} />
          <Route path='/register' element={<RegisterForm />} />
          <Route path='/chat/:userID' element={<Chat />} />
          <Route path='/magazine' element={<Magazine />} />
          <Route path='/travelplanner' element={<TripPlanner />} />
          <Route path='/dashboard' element={<Dashboard />} />
          <Route path='/plannerresult' element={<PlannerResultPage />} />
          <Route path='/profile' element={<Profile />} />
        </Routes>
      </Router>
      <header className="App-header">
        {getComp()}
      </header>
    </div>
  );
}

export default App;
