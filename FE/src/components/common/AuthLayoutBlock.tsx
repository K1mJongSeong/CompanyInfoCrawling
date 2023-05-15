"use client";

import { useAuth } from "@/contexts/auth.context";
import { redirect } from "next/navigation";

export default function AuthLayoutBlock({
  children,
}: {
  children: React.ReactNode;
}) {
  const { user } = useAuth();
  if (user) {
    redirect("/");
  }
  return <>{children}</>;
}
