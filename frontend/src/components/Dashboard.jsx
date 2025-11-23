import React, {useEffect, useState} from 'react'
import api from '../services/api'

export default function Dashboard({token}){
  const [student,setStudent]=useState({attendance:80,past_marks:70,activities_score:5})
  const [risk,setRisk]=useState(null)

  async function check(){
    const res = await api.post('/predict', student, {headers:{Authorization:`Bearer ${token}`}})
    setRisk(res.data)
  }

  useEffect(()=>{check()},[])
  return (
    <div>
      <h1 className="text-2xl font-semibold mb-4">Dashboard — Haldia Institute of Technology</h1>
      <div className="bg-white p-4 rounded shadow">
        <div>Risk: {risk ? JSON.stringify(risk) : 'Loading...'}</div>
      </div>
    </div>
  )
}
