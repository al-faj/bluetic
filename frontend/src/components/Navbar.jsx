import React from 'react'
export default function Navbar(){
  return (
    <nav className="flex items-center justify-between p-4 bg-white dark:bg-gray-800">
      <div className="flex items-center">
        <img src="/logo.png" alt="logo" className="h-10 mr-3"/>
        <div className="font-semibold">Haldia Institute of Technology</div>
      </div>
      <div>Student Risk Predictor</div>
    </nav>
  )
}
