"use client";
import React, { createContext, useContext } from "react";
import useAuthHook from "@/hooks/useAuth";

interface InAuthUserContext {
  user: { email: string; data: { user_name: string } } | null;
  loading: boolean;
  signIn: ({ email, pw }: { email: string; pw: string }) => void;
  signOut: () => void;
}

const AuthUserContext = createContext<InAuthUserContext>({
  user: null,
  loading: true,
  signIn: async () => {},
  signOut: async () => {},
});

export const AuthUserProvider = function ({
  children,
}: {
  children: React.ReactNode;
}) {
  const auth = useAuthHook();
  return (
    <AuthUserContext.Provider value={auth}>{children}</AuthUserContext.Provider>
  );
};

export const useAuth = () => useContext(AuthUserContext);
