import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';

import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

export const GET: RequestHandler = async () => {
    try {
        const { stdout } = await execAsync('python backend/fetch_schemas.py');
        const schemas = JSON.parse(stdout);
        return json(schemas);
    } catch (error) {
        console.error('Error fetching schemas:', error);
        return json({ error: 'Failed to fetch schemas' }, { status: 500 });
    }
};


export const PUT: RequestHandler = async ({ request }) => {
    const schema = await request.json();
    try {
        const { stdout } = await execAsync(`python backend/update_schema.py '${JSON.stringify(schema)}'`);
        const result = JSON.parse(stdout);
        return json(result);
    } catch (error) {
        console.error('Error updating schema:', error);
        return json({ success: false, message: 'Failed to update schema' }, { status: 500 });
    }
};

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