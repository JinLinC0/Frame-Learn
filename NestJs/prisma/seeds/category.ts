import { PrismaClient } from "@prisma/client";
import { Random } from "mockjs";
import { create } from "../helper";

export async function category() {
    await create(5, async (prisma: PrismaClient) => {
        await prisma.category.create({
            data: {
                title: Random.ctitle(2, 5)
            },
        });
    })
}