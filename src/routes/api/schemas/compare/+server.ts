import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

export const POST: RequestHandler = async ({ request }) => {
    const { schema1, schema2 } = await request.json();
    try {
        const { stdout } = await execAsync(`python backend/compare_schemas.py "${schema1}" "${schema2}"`);
        const comparisonResult = JSON.parse(stdout);
        return json(comparisonResult);
    } catch (error) {
        console.error('Error comparing schemas:', error);
        return json({ error: 'Failed to compare schemas' }, { status: 500 });
    }
};
