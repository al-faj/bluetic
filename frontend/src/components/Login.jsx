import React, {useState} from 'react'
import api from '../services/api'

export default function Login({onLogin}){
  const [email,setEmail]=useState('')
  const [code,setCode]=useState('')
  const [step,setStep]=useState(0)

  async function requestOtp(){
    await api.post('/auth/request-otp',{email})
    setStep(1)
  }
  async function verify(){
    const res = await api.post('/auth/verify-otp',{email,code})
    onLogin(res.data.access_token)
  }

  return (
    <div className="max-w-md mx-auto bg-white dark:bg-gray-800 p-6 rounded-lg shadow">
      <img src="/logo.png" alt="Haldia Institute of Technology" className="h-16 mx-auto"/>
      <h2 className="text-center text-xl font-semibold mt-2">Haldia Institute of Technology — Student Risk Predictor</h2>
      {step===0 ? (
        <div>
          <input value={email} onChange={e=>setEmail(e.target.value)} placeholder="College email" className="w-full p-2 mt-4 rounded border"/>
          <button onClick={requestOtp} className="w-full mt-4 p-2 rounded bg-sky-600 text-white">Send OTP</button>
        </div>
      ) : (
        <div>
          <input value={code} onChange={e=>setCode(e.target.value)} placeholder="Enter OTP" className="w-full p-2 mt-4 rounded border"/>
          <button onClick={verify} className="w-full mt-4 p-2 rounded bg-green-600 text-white">Verify & Login</button>
        </div>
      )}
    </div>
  )
}
