"use client";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { Button } from "../components/button";
import {
  Form,
  FormField,
  FormItem,
  FormLabel,
  FormControl,
  FormMessage,
} from "../components/Form";
import { Input } from "../components/Input";
import logo from "../assets/logo.svg";
import { ArrowLeft } from "@phosphor-icons/react";

const formSchema = z.object({
  username: z.string().min(2, {
    message: "Campo obrigatório",
  }),
  password: z.string().min(2, {
    message: "Campo obrigatório",
  }),
});

function onSubmit(values: z.infer<typeof formSchema>) {
  console.log(values);
}

export default function Login() {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      username: "",
      password: "",
    },
  });

  return (
    <section className="w-full min-h-screen bg-green-700 flex justify-center items-center px-4">
      <div className="bg-white w-full max-w-lg p-8 rounded-lg shadow-md shrink-0">
        <a
          href="/"
          className="p-3 items-center flex gap-3 border border-gray-400 w-max rounded-lg text-green-700"
        >
          <ArrowLeft className="w-6 h-6" />
          <span className="text-base">Voltar</span>
        </a>
        <div className="mb-8">
          <img
            src={logo}
            className="w-40 h-40 object-fill mx-auto"
            alt="Logo"
          />
          <h2 className="text-2xl text-center">Entrar na sua conta</h2>
          <p className="text-center text-gray-600">
            Preencha as informações abaixo para entrar na sua conta.
          </p>
        </div>
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-4">
            <FormField
              control={form.control}
              name="username"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Usuário</FormLabel>
                  <FormControl>
                    <Input placeholder="Insira seu username" {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
            <FormField
              control={form.control}
              name="password"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Senha</FormLabel>
                  <FormControl>
                    <Input placeholder="Insira sua senha" {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
            <a
              className="block text-right text-green-700 cursor-pointer transition-all hover:text-green-600"
              href="#"
            >
              Esqueceu a senha?
            </a>
            <div className="flex items-center justify-between">
              <Button type="submit">Entrar</Button>
            </div>
          </form>
        </Form>
        <a
          href="/register"
          className="mt-4 text-center text-sm cursor-pointer hover:opacity-75 transition-opacity block "
        >
          <span>Não tem conta? </span>
          <span className="text-green-700 underline">Criar conta</span>
        </a>
      </div>
    </section>
  );
}
