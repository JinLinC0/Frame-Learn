import { PrismaClient } from "@prisma/client";
import { Random } from "mockjs";
import { create } from "../helper";

export function user() {
    create(20, async (prisma: PrismaClient) => {
        await prisma.user.create({
            data: {
                email: Random.email(),
                password: Random.string(),
                name: Random.string(),
                avatar: Random.image("200x200"),
                github: Random.url()
            },
        });
    })
}