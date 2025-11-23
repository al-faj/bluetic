import React, {useState} from 'react'
import Login from './components/Login'
import Dashboard from './components/Dashboard'
import Navbar from './components/Navbar'

export default function App(){
  const [token, setToken] = useState(localStorage.getItem('token'))
  return (
    <div className="min-h-screen bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-gray-100">
      <Navbar />
      <main className="p-6">
        {!token ? <Login onLogin={t=>{setToken(t); localStorage.setItem('token',t)}}/> : <Dashboard token={token} />}
      </main>
    </div>
  )
}
