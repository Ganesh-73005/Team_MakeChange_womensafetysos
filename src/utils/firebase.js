import { initializeApp } from "firebase/app";
import { getAuth, onAuthStateChanged, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut as firebaseSignOut } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyB9t2Wgvbl_NDa2dSMv5-NGkgWdLfwc614",
  authDomain: "safeher-2b129.firebaseapp.com",
  projectId: "safeher-2b129",
  storageBucket: "safeher-2b129.appspot.com",
  messagingSenderId: "309435057390",
  appId: "1:309435057390:web:d0863974357d768955dfff",
  measurementId: "G-KPQFFTNJZV"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Export functions and variables
export const auth = getAuth(app);

// Export the initialize function if you want to call it manually
export function initialize() {
  if (!app) {
    initializeApp(firebaseConfig);
  }
}

export function attachAuthListener(handler) {
  return onAuthStateChanged(auth, handler);
}

export async function createNewUser(email, password) {
  return createUserWithEmailAndPassword(auth, email, password);
}

export async function signIn(email, password) {
  return signInWithEmailAndPassword(auth, email, password);
}

export async function signOut() {
  return firebaseSignOut(auth);
}
