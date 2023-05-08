'use client'
import { AcountContainer, AcountCard } from "@/components/account/styles";

export default function AccountContainer({ id }: { id: string }) {
  return <AcountContainer><AcountCard>{id}</AcountCard></AcountContainer>;
}
