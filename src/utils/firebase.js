import { initializeApp } from "firebase/app";
import { getAuth, onAuthStateChanged, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut as firebaseSignOut } from "firebase/auth";

const firebaseConfig = {
 
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
