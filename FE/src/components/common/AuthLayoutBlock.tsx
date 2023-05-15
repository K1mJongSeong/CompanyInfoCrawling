"use client";

import { useAuth } from "@/contexts/auth.context";
import { redirect } from "next/navigation";

export default function AuthLayoutBlock({
  Authentication,
  children,
}: {
  Authentication: boolean;
  children: React.ReactNode;
}) {
  const { user } = useAuth();

  if (!Authentication && user) {
    redirect("/");
  }
  if (Authentication && !user) {
    redirect("/");
  }
  return <>{children}</>;
}
